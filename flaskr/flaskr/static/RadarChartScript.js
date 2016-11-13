var w = 500,
	h = 500;

var colorscale = d3.scale.category10();
var currentText = ""

$.getJSON($SCRIPT_ROOT + '/getCurrentData', function (data) {
	createGraph(data["tones"]);
	currentText = data["text"];
	showStats(currentText);
});

function showStats(text) {
	console.log(text)
	$('#dailystats').append(text);
};

function createGraph(emotionVals) {
	axes = [];
	for (var key in emotionVals){
		var attrValue = emotionVals[key];
	    axes.push({axis:key, value:attrValue});
	}
	// console.log(axes);
	var d = [axes];

	//Options for the Radar chart, other than default
	var mycfg = {
	  w: w,
	  h: h,
	  maxValue: 0.6,
	  levels: 6,
	  ExtraWidthX: 200
	}

	//Call function to draw the Radar chart
	//Will expect that data is in %'s
	RadarChart.draw("#chart", d, mycfg);

	////////////////////////////////////////////
	/////////// Initiate legend ////////////////
	////////////////////////////////////////////

	var svg = d3.select('#body')
		.selectAll('svg')
		.append('svg')
		.attr("width", w)
		.attr("height", h)
}
