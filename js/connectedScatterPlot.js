function drawConnectedScatter(gender, period, player){

  // set the dimensions and margins of the graph
  var margin = {top: 10, right: 20, bottom: 70, left: 60},
      width = 1300 - margin.left - margin.right,
      height = 240 - margin.top - margin.bottom;

  // append the svg object to the body of the page
  var svg = d3.select(".mainWrapper")
    .append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
      .attr("class", "linePlot")
      .attr("transform", "translate(-40, -120)")
    .append("g")
      .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");

  let divTooltip = d3.select("body").append("div").attr("class", "tooltip").style("opacity", 0);

  var x = d3.scaleLinear()
    .range([ 0, width]);

  var xAxis = d3.axisBottom(x);
  xAxis.tickValues([]);

  svg.append("g")
    .attr("class", "xAxis")
    .attr("transform", "translate(0," + height + ")")
    .style("stroke", "#ffffff")
    .style("stroke-width", "0.5px")
    .call(xAxis)
    .append("text")
    .attr("class", "label")
    .attr("x", width)
    .attr("y", -6)
    .style("text-anchor", "end")
    .style("fill", "#ffffff")
    .text("Year");


  var y = d3.scaleLinear()
    .domain( [100, 1])
    .range([ height, 0 ]);
  svg.append("g")
    .attr("class", "yAxis")
    .style("stroke", "#ffffff")
    .style("stroke-width", "0.5px")
    .call(d3.axisLeft(y))
    .append("text")
      .attr("class", "label")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .style("fill", "#ffffff")
      .text("Position");

    if(player != ""){
      d3.csv("../data/preprocessed/line/"+ gender +"_rankings_trend_"+ period +".csv", function(data) {
         var years = [];
         var positions = [];
         data.forEach(function(row){
           if(player == row["name"]){
             years = row["year"];
             positions = row["position"];
           }
         });

         var domain = years.split(",");
         for(i=0; i < domain.length; i++){
           domain[i].toString();
           domain[i] = domain[i].substring(1);
         }
         domain[domain.length-1] = domain[domain.length-1].slice(0, -1);

         for(i=0; i < domain.length; i++){
           domain[i] = parseInt(domain[i]);
         }

         domain.sort(function(a, b){return a-b});

         for(i=0; i < domain.length; i++){
             domain[i] = domain[i].toString();
         }

         var pos = positions.split(",");
         for(i=0; i < pos.length; i++){
           pos[i].toString();
           pos[i] = pos[i].substring(1);
         }
         pos[pos.length-1] = pos[pos.length-1].slice(0, -1);

         var x = d3.scaleLinear()
           .domain([parseInt(domain[0]), parseInt(domain[domain.length-1])])
           .range([ 0, width]);

         var xAxis = d3.axisBottom(x);
         xAxis.tickFormat(d3.format('0'));

         svg.append("g")
           .attr("class", "xAxis")
           .attr("transform", "translate(0," + height + ")")
           .style("stroke", "#ffffff")
           .style("stroke-width", "0.5px")
           .call(xAxis)
           .append("text")
           .attr("class", "label")
           .attr("x", width)
           .attr("y", -6)
           .style("text-anchor", "end")
           .style("fill", "#ffffff")
           .text("Year");

        svg.append("path")
          .datum(d3.zip(domain, pos))
          .attr("fill", "none")
          .attr("stroke", "#69b3a2")
          .attr("stroke-width", 1.5)
          .attr("d", d3.line()
            .x(function(d) { return x(parseInt(d[0])) })
            .y(function(d) {
              if(parseInt(d[1]) > 100){
                return y(100);
              }
              else{
                return y(parseInt(d[1]));
              }
            }))

          svg
            .append("g")
            .selectAll("dot")
            .data(d3.zip(domain, pos))
            .enter()
            .append("circle")
              .attr("cx", function(d) { return x(parseInt(d[0])) } )
              .attr("cy", function(d) {
                if(parseInt(d[1]) > 100){
                  return y(100);
                }
                else{
                  return y(parseInt(d[1]))
                }
              })
              .attr("r", 5)
              .attr("fill", "#69b3a2")
              .on("mouseover", function (d) {
                  divTooltip.style("opacity", 1);
                  divTooltip.html(`<span>Year: ${parseInt(d[0])}</span><br/><span>Best position: ${parseInt(d[1])}</span><br/>`)
                      .style("top", `${d3.event.pageY - 50}px`);
              })
              .on("mouseout", function (){
                  divTooltip.style("opacity", 0);
              })
              .on("mousemove", function() {
                  divTooltip.style("left", `${d3.event.pageX}px`)
                      .style("top", `${d3.event.pageY - 90}px`);
              });

            svg.append("text")
                .attr("x", 400)
                .attr("y", 220)
                .text(player + " best positions over the years")
                .attr("fill", "#b1c7e2")
                .attr("font-size", 16);
      });
}
}

function updateConnectedScatterPlot(gender, period, player){
  removeConnectedScatter();
  drawConnectedScatter(gender, period, player);
}

function removeConnectedScatter(){
  d3.select(".linePlot").remove();
}
