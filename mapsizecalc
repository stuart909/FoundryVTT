//Written By: Stuart Anderson
//Input background or map X-Y as it and measure out the diameter, in pixels of...
//what you would presume is the diameter of a size 0 character pog.
//Will output a chat message directing GM to input new Map X, Y override.
//This assumes you want to use 50x50 gridless or grid maps with 1" as unit of measure.

let grid_menu = new Dialog({
	title: `Map Size Calculator`,
	content: `
		<form>
			<div style="display: flex; width: 100%; margin-bottom: 10px">
            	<label for="mapX" style="white-space: nowrap; margin-right: 10px; padding-top:4px">Map X: </label>
            	<input type="text" id="mapX" name="mapX" />
            	<label for="mapY" style="white-space: nowrap; margin-right: 10px; padding-top:4px">Map Y: </label>
            	<input type="text" id="mapY" name="mapY" />
            	<label for="s0" style="white-space: nowrap; margin-right: 10px; padding-top:4px">Size 0 Diameter: </label>
            	<input type="text" id="s0" name="s0" />
            </div>
		</form>
	`,
	buttons: {
		yes: {
			icon: "<i class='fas fa-check'></i>",
			label: `Submit`,
			callback: (html) => {
				if (game.user.isGM) {
					let mapX = parseInt(html.find('input#mapX').val());
					let mapY = parseInt(html.find('input#mapY').val());
					let s0 = parseInt(html.find('input#s0').val());
					let n = s0/50;
					mapX*=n;
					mapY*=n;
					ChatMessage.create({
                                speaker: {
                                    alias: 'Map Measure'
                                },
                                content: 'Map X: '+mapX+'<br>Map Y: '+mapY
                    });
				}
			}
		},
		no: {
			icon: "<i class='fas fa-times'></i>",
			label: `Cancel`
		},
	},
	default: "yes"
}).render(true);
