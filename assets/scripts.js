if (!window.dash_clientside) {
    window.dash_clientside = {};
}
const stringify = (id) => typeof id === "string" ? id : JSON.stringify(id, Object.keys(id).sort());

window.dash_clientside.draggable = {
    make_draggable: function(column_ids, store_card_id, store_column_id, store_old_column_id, store_position_id) {

        setTimeout(function() {
            let elements = [];

            for(let idx = 0; idx < column_ids.length; idx++){
                let id = column_ids[idx];
                console.log(`Making ${stringify(id)} work with Dragula`);
                var el = document.getElementById(stringify(id));
                window.console.log(el);
                elements.push(el);
            }
            dragula(elements)
                .on('drop', function (element, target, source, sibling){
                    console.log(`Moved card`)
                    console.log("element: ", element)
                    console.log("target: ", target)
                    console.log("source: ", source)
                    console.log("sibling: ", sibling)

                    console.log("\nFormatted:")
                    let element_id = JSON.parse(element.id).index
                    let column_id = JSON.parse(target.id).index
                    let old_column_id = JSON.parse(source.id).index
                    let position = sibling == null ? -1 : JSON.parse(sibling.id).index
                    console.log("element id: ", element_id)
                    dash_clientside.set_props(store_card_id, {"data": element_id})
                    console.log("new column: ", column_id)
                    dash_clientside.set_props(store_column_id, {"data": column_id})
                    console.log("old column: ", old_column_id)
                    dash_clientside.set_props(store_old_column_id, {"data": old_column_id})
                    console.log("Position: ", position == -1 ? "Last" : `Higher than card with ID ${position}`)
                    dash_clientside.set_props(store_position_id, {"data": position})

//                    console.log(source.id, source.childNodes)
//                    document.getElementById(stringify(source.id)).replaceChildren(new dash_mantine_components.Container([new dash_mantine_components.Text("test")]))
//                    document.getElementById(stringify(target.id)).replaceChildren([])
                }
            );


        }, 1);

        return Array.from(column_ids).map((item) => dash_clientside.no_update)
    }
}