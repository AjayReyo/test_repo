function calculate(){
	var buy=Number(document.getElementById("buy_input").value);
	var sell=Number(document.getElementById("sell_input").value);
	var quantity=Number(document.getElementById("quantity_input").value);
	var turnover=(buy+sell)*quantity;
	var brokerage=0.01/100*turnover;
	brokerage=Number(brokerage.toFixed(2));
	var stt=0.025/100*sell*quantity;
	stt = Number(Math.ceil(stt));
	var exch=0.00325/100*turnover
	exch=Number(exch.toFixed(2));
	var gst=18/100*(brokerage+exch);
	gst=Number(gst.toFixed(2));
	var duty =0.01/100*turnover;
	duty=Number(duty.toFixed(2));
	var sebi=15/10000000*turnover;
	sebi=Number(sebi.toFixed(2));
	var charges=Number(brokerage+stt+exch+gst+duty+sebi);
	document.getElementById("charges").innerHTML = charges;
}
function test(){
	$(document).ready(function(){
		$("input").keyup(function(){
			var primaryincome = $("#buy").val();
			var otherincome = $("#sell").val();
			var total = parseInt(primaryincome) + parseInt(otherincome);
			$("#total").text(total);
			});
			})
}
