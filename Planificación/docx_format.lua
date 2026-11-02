-- Índice con hipervínculos reales (no un campo TOC vacío) y sin el
-- índice manual del Markdown, que solo sirve para leer el .md.

-- Quita el índice manual y devuelve la posición que ocupaba, para poner
-- allí el índice del Word: después de la portada y antes del apartado 1.
local function skip_manual_index(blocks)
  local out = {}
  local position = nil
  for _, block in ipairs(blocks) do
    local drop = block.t == "Div" and block.classes:includes("manual-index")
    if drop then
      position = position or (#out + 1)
    else
      table.insert(out, block)
    end
  end
  return out, position
end

local function page_break()
  return pandoc.RawBlock("openxml", '<w:p><w:r><w:br w:type="page"/></w:r></w:p>')
end

local function collect_headers(blocks)
  local headers = {}
  local started = false
  for _, block in ipairs(blocks) do
    if block.t == "Header" and block.level <= 3 and block.identifier ~= "" then
      local text = pandoc.utils.stringify(block)
      if not started and text:match("^1%. Introducción") then
        started = true
      end
      if started and block.identifier ~= "indice" then
        table.insert(headers, block)
      end
    end
  end
  return headers
end

-- Devuelve la lista de ítems y el índice siguiente.
local function nested_list(headers, index, level)
  local items = {}
  while index <= #headers do
    local header = headers[index]
    if header.level < level then
      break
    end
    if header.level > level then
      index = index + 1
    else
      local link = pandoc.Link(
        pandoc.utils.stringify(header),
        "#" .. header.identifier
      )
      index = index + 1
      local item = { pandoc.Plain({ link }) }
      if index <= #headers and headers[index].level > level then
        local sub
        sub, index = nested_list(headers, index, headers[index].level)
        if #sub > 0 then
          table.insert(item, pandoc.BulletList(sub))
        end
      end
      table.insert(items, item)
    end
  end
  return items, index
end

function Pandoc(doc)
  local position
  doc.blocks, position = skip_manual_index(doc.blocks)
  local headers = collect_headers(doc.blocks)
  if #headers == 0 then
    return doc
  end
  local items = nested_list(headers, 1, headers[1].level)
  local intro = pandoc.Para({
    pandoc.Str("Cada"),
    pandoc.Space(),
    pandoc.Str("entrada"),
    pandoc.Space(),
    pandoc.Str("abre"),
    pandoc.Space(),
    pandoc.Str("el"),
    pandoc.Space(),
    pandoc.Str("apartado"),
    pandoc.Space(),
    pandoc.Str("correspondiente."),
  })
  local index_header = pandoc.Header(1, "Índice", pandoc.Attr("indice", {}, {}))
  if position == nil then
    -- Sin índice manual: el índice va antes del apartado 1.
    position = 1
    for i, block in ipairs(doc.blocks) do
      if block.t == "Header" and pandoc.utils.stringify(block):match("^1%. Introducción") then
        position = i
        break
      end
    end
  end
  -- Portada, salto de página, índice, salto de página y apartado 1.
  local index_blocks = { page_break(), index_header, intro, pandoc.BulletList(items), page_break() }
  for offset, block in ipairs(index_blocks) do
    table.insert(doc.blocks, position + offset - 1, block)
  end
  return doc
end
