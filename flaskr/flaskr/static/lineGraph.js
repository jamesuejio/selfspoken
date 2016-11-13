$.getJSON($SCRIPT_ROOT + '/getLineVals', function (data) {
  InitChart(data);
});
function InitChart(data) {
    console.log(data)
    var data1 = data["Anger"]
    console.log(data1)


    // var data2 = [{
    //     "sale": "152",
    //     "year": "2000"
    // }, {
    //     "sale": "189",
    //     "year": "2002"
    // }, {
    //     "sale": "179",
    //     "year": "2004"
    // }, {
    //     "sale": "199",
    //     "year": "2006"
    // }, {
    //     "sale": "134",
    //     "year": "2008"
    // }, {
    //     "sale": "176",
    //     "year": "2010"
    // }];

    // Parse the date / time
    var parseDate = d3.time.format("%a %b %d %X %Y").parse;

    var vis = d3.select("#visualisation"),
        WIDTH = 1000,
        HEIGHT = 500,
        MARGINS = {
            top: 20,
            right: 50,
            bottom: 20,
            left: 400
        },

        xScale = d3.time.scale().range([MARGINS.left, WIDTH - MARGINS.right]),

        yScale = d3.scale.linear().range([HEIGHT - MARGINS.top, MARGINS.bottom]),

        xAxis = d3.svg.axis()
        .scale(xScale).orient("bottom").ticks(5),

        yAxis = d3.svg.axis()
        .scale(yScale)
        .orient("left");


    vis.append("svg:g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + (HEIGHT - MARGINS.bottom) + ")")
        .call(xAxis);

    vis.append("svg:g")
        .attr("class", "y axis")
        .attr("transform", "translate(" + (MARGINS.left) + ",0)")
        .call(yAxis);

    var lineGen = d3.svg.line()
        .x(function(d) {
            console.log(parseDate(d.time))
            return xScale(parseDate(d.time));
        })
        .y(function(d) {
            return yScale(d.count.toString());
        })
        .interpolate("basis");

    vis.append('svg:path')
        .attr('d', lineGen(data1))
        .attr('stroke', 'green')
        .attr('stroke-width', 2)
        .attr('fill', 'none');

    // vis.append('svg:path')
    //     .attr('d', lineGen(data2))
    //     .attr('stroke', 'blue')
    //     .attr('stroke-width', 2)
    //     .attr('fill', 'none');

}
