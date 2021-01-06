//Written By: Stuart Anderson
//This is a finance program that is used in my campaign to add or remove funds from an actor and report bank balance.
//Actor must be set in the company variable and reference an actual actor name.  Default is "BC Organization".
//Supports multiple currencies.
//Currency rate, exchange, and rate changes is TODO

let company = game.actors.getName("BC Organization");
let w = company.data.flags.world;
let summary = {};
let days = parseInt(company.getFlag('world','days'));
let currency_data = ['cred','isc','gkd','urd','nad','ced','tcd','ucd'];
currency_data.forEach(function(item,index){
    if (w.hasOwnProperty(item)){
        summary[item]=w[item];
    }
});
let cashOptions = game.user.isGM ? `
    <div style="display: inline-block; width: 100%; margin-bottom: 10px">
    	<label for="cash-options" style="margin-right: 10px">Cash Option:</label>
    	<select id="cash-options" />
    		<option value="report">Report</option>
    		<option value="add">Add</option>
    		<option value="remove">Remove</option>
    		<option value="exchange">Exchange</option>
    		<option value="rates">Rates</option>
    	</select>
    </div>
    <br />
` : '';

let addcash_menu = new Dialog({
	title: `Add Cash Menu`,
	content: `
		<form>
			<div style="display: flex; width: 100%; margin-bottom: 10px">
            	<label for="currency" style="white-space: nowrap; margin-right: 10px; padding-top:4px">Currency: </label>
            	<input type="text" id="currency" name="currency" />
            	<label for="amount" style="white-space: nowrap; margin-right: 10px; padding-top:4px">Amount: </label>
            	<input type="text" id="amount" name="amount" />
            </div>
            <div style="display: flex; width: 100%; margin-bottom: 10px">
                <table>
                    <tr>
                        <td>Earth Credits: cred</td>
                        <td>Intergalactic Space Credits: isc</td>
                    </tr>
                    <tr>
                        <td>Gobli Kingdom Dollar: gkd</td>
                        <td>Ur Dollar: urd</td>
                    </tr>
                    <tr>
                        <td>N. Goblin Alliance Dollar: nad</td>
                        <td>Celestial Denar: ced</td>
                    </tr>
                    <tr>
                        <td>Three Cities Dollar: tcd</td>
                        <td>United Cities Dollar: ucd</td>
                    </tr>
                </table>
            </div>
		</form>
	`,
	buttons: {
		yes: {
			icon: "<i class='fas fa-check'></i>",
			label: `Submit`,
			callback: (html) => {
				if (game.user.isGM) {
					let currency = html.find('input#currency').val();
					let amount = parseInt(html.find('input#amount').val());
					if (currency_data.includes(currency)) {
					    let msg = '';
					    try {
					        let val = parseInt(company.getFlag('world',currency));
					        if (isNaN(val)){
					            msg+='<br>Deposited: ₢'+amount+' '+currency;
					            msg+='<br>New Balance: ₢'+amount+' '+currency;
					            company.setFlag('world',currency,amount);
					            ChatMessage.create({
                                    speaker: {
                                        alias: 'Bank Statement'
                                    },
                                    content: msg
                                });
					        }else{
    					        let sum = val+amount;
    					        company.setFlag('world',currency,sum);
    					        msg+='Balance: '+val+' '+currency;
    					        msg+='<br>Deposited: ₢'+amount+' '+currency;
    					        msg+='<br>New Balance: ₢'+sum+' '+currency;
    					        ChatMessage.create({
                                    speaker: {
                                        alias: 'Bank Statement'
                                    },
                                    content: msg
                                });
					        }
					    }catch(error){
					        msg+='<br>Deposited: ₢'+amount+' '+currency;
					        msg+='<br>New Balance: ₢'+amount+' '+currency;
					        company.setFlag('world',currency,amount);
					        ChatMessage.create({
                                speaker: {
                                    alias: 'Bank Statement'
                                },
                                content: msg
                            });
					    }
					}else{
					    main_menu.render(True)
					}
				}
			}
		},
		no: {
			icon: "<i class='fas fa-times'></i>",
			label: `Cancel`,
			callback: (html) => {
				if (game.user.isGM) {
					main_menu.render(true);
				}
			}
		},
	},
	default: "yes"
})
let removecash_menu = new Dialog({
	title: `Remove Cash Menu`,
	content: `
		<form>
			<div style="display: flex; width: 100%; margin-bottom: 10px">
            	<label for="currency" style="white-space: nowrap; margin-right: 10px; padding-top:4px">Currency: </label>
            	<input type="text" id="currency" name="currency" />
            	<label for="amount" style="white-space: nowrap; margin-right: 10px; padding-top:4px">Amount: </label>
            	<input type="text" id="amount" name="amount" />
            </div>
            <div style="display: flex; width: 100%; margin-bottom: 10px">
                <table>
                    <tr>
                        <td>Earth Credits: cred</td>
                        <td>Intergalactic Space Credits: isc</td>
                    </tr>
                    <tr>
                        <td>Gobli Kingdom Dollar: gkd</td>
                        <td>Ur Dollar: urd</td>
                    </tr>
                    <tr>
                        <td>N. Goblin Alliance Dollar: nad</td>
                        <td>Celestial Denar: ced</td>
                    </tr>
                    <tr>
                        <td>Three Cities Dollar: tcd</td>
                        <td>United Cities Dollar: ucd</td>
                    </tr>
                </table>
            </div>
		</form>
	`,
	buttons: {
		yes: {
			icon: "<i class='fas fa-check'></i>",
			label: `Submit`,
			callback: (html) => {
				if (game.user.isGM) {
					let currency = html.find('input#currency').val();
					let amount = parseInt(html.find('input#amount').val());
					if (currency_data.includes(currency)) {
					    let msg = '';
					    try {
					        let val = parseInt(company.getFlag('world',currency));
					        if (isNaN(val)){
					            msg+='<br>No currency of this type';
					            ChatMessage.create({
                                    speaker: {
                                        alias: 'Bank Statement'
                                    },
                                    content: msg
                                });
					        }else{
    					        if(val >= amount){
									let sum = val-amount;
									company.setFlag('world',currency,sum);
									msg+='Balance: ₢'+val+' '+currency;
									msg+='<br>Withdrew: ₢'+amount+' '+currency;
									msg+='<br>New Balance: ₢'+sum+' '+currency;
									ChatMessage.create({
										speaker: {
											alias: 'Bank Statement'
										},
										content: msg
                                	});
								}else{
									msg+='Not enough currency';
									ChatMessage.create({
										speaker: {
											alias: 'Bank Statement'
										},
										content: msg
                                	});
								}
					        }
					    }catch(error){
					        msg+='Bank error';
					        ChatMessage.create({
                                speaker: {
                                    alias: 'Bank Statement'
                                },
                                content: msg
                            });
					    }
					}else{
					    main_menu.render(True)
					}
				}
			}
		},
		no: {
			icon: "<i class='fas fa-times'></i>",
			label: `Cancel`,
			callback: (html) => {
				if (game.user.isGM) {
					main_menu.render(true);
				}
			}
		},
	},
	default: "yes"
})



let main_menu = new Dialog({
	title: `Finance Main Menu`,
	content: `
		<form>
			${cashOptions}
		</form>
	`,
	buttons: {
		yes: {
			icon: "<i class='fas fa-check'></i>",
			label: `Submit`,
			callback: (html) => {
				if (game.user.isGM) {
					let selection = html.find('select#cash-options').val();
					if (selection == 'add') {
					    addcash_menu.render(true);
					}else if(selection == 'remove'){
					    removecash_menu.render(true);
					}else if(selection == 'report'){
					    let msg = 'Balance:';
						console.log('109 '+ Object.entries(summary))
						for (const [k,v] of Object.entries(summary)) {
						    if (parseInt(v) > 0){msg+='<br>₢'+v+' '+k;}
						}
						ChatMessage.create({
							speaker: {
								alias: 'Bank Statement'
							},
							content: msg
                    	});
					}
				}
			}
		},
		no: {
			icon: "<i class='fas fa-times'></i>",
			label: `Cancel`
		},
	},
	default: "yes"
})

main_menu.render(true);
