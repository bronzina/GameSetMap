wta = {
    "wtaall": "data/preprocessed/bar/wta_grandSlams_all.csv",
    "wta2021": "data/preprocessed/bar/wta_grandSlams_2021.csv",
    "wta2020": "data/preprocessed/bar/wta_grandSlams_2020.csv",
    "wta2010": "data/preprocessed/bar/wta_grandSlams_2010.csv",
    "wta2000": "data/preprocessed/bar/wta_grandSlams_2000.csv",
    "wta1990": "data/preprocessed/bar/wta_grandSlams_1990.csv",
    "wta1980": "data/preprocessed/bar/wta_grandSlams_1980.csv"
}

atp = {
  "atpall": "data/preprocessed/bar/atp_grandSlams_all.csv",
  "atp2021": "data/preprocessed/bar/atp_grandSlams_2021.csv",
  "atp2020": "data/preprocessed/bar/atp_grandSlams_2020.csv",
  "atp2010": "data/preprocessed/bar/atp_grandSlams_2010.csv",
  "atp2000": "data/preprocessed/bar/atp_grandSlams_2000.csv",
  "atp1990": "data/preprocessed/bar/atp_grandSlams_1990.csv",
  "atp1980": "data/preprocessed/bar/atp_grandSlams_1980.csv"
}


//Initially, value = "atp" and iter = 0
function drawTitlesFinalsRecords(value, iter, period) {

  // set the dimensions of the canvas
  let margin = {top: 0, right: 20, bottom: 0, left: 60},
      width = 1300 - margin.left - margin.right,
      height = 500 - margin.top - margin.bottom;

  // set the ranges
  let x = d3.scaleBand().rangeRound([0, 50]),
      y = d3.scaleLinear().rangeRound([height / 2, 50]);

  let xPrize = d3.scaleBand().rangeRound([0, 50]),
      yPrize = d3.scaleLinear().rangeRound([height / 2, 10]);

  let colorScheme = ["#e6b800", "#b30000"];
  let color = d3.scaleOrdinal(colorScheme);

  let colorScehemeGrandSlam = ["#fffed3", "#efee6a", "#93c96e", "#54a977", "#278074", "#307c87", "#2d5e84", "#04487c"];
  let colorGrandSlam = d3.scaleLinear().range(colorScehemeGrandSlam);

  d3.select(".tooltip").attr("opacity",1).transition().duration(100).attr("opacity",0).remove();
  d3.select(".lineCircleChartDiv").attr("opacity",1).transition().duration(100).attr("opacity",0).remove();

  //Tooltip for hover on barChart
  let divTooltip = d3.select("body").append("div").attr("class", "tooltip").style("opacity", 0);

  // add the SVG element
  let svg = d3.select(".mainWrapper").append("div").attr("class", "lineCircleChartDiv").append("svg").attr("class", "lineCircleChart")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom);

  svg.append("text")
      .attr("x", 350)
      .attr("y", 15)
      .text(" List of career achievements by top 10 tennis players who have played")
      .attr("fill", "#b1c7e2")
      .attr("font-size", 14);

  svg.append("text")
      .attr("x", 350)
      .attr("y", 35)
      .text("the highest number of Grand Slam finals in the " + value.toUpperCase() + " ranking (1980-2021).")
      .attr("fill", "#b1c7e2")
      .attr("font-size", 14);

  svg.append("text")
      .attr("x", 350)
      .attr("y", 55)
      .text("Click on a player's name to show its best ranking over the years.")
      .attr("fill", "#b1c7e2")
      .attr("font-size", 14);

  if (iter === 0) {
      svg.attr("opacity", 0).transition().duration(1800).attr("opacity", 1);
  }

  svg.attr("opacity",0).transition().duration(100).attr("opacity",1);

  drawLegendLineCircleChart(svg, width);

  let players = [];

  if(gender == "atp"){
    d3.queue()
      .defer(d3.csv, atp["atp" + period])
      .await(ready);
  }

  else{
    d3.queue()
      .defer(d3.csv, wta["wta" + period])
      .await(ready);
  }


  function ready(error, data) {
      if (error) { console.info(error);}
      let grandSlams = [];
      data.forEach(function(player) {
            if(!players.includes(player)){
              players.push(player);
            }

      });

      let sortedPlayers = players.sort(function(a, b){
        if(a.grandSlamTitles != b.grandSlamTitles){
          return b.grandSlamTitles - a.grandSlamTitles;
        }
        else{
          return b.grandslamFinals - a.grandslamFinals;
        }
      });

      let top10Players = [];

      for(i=0; i < 10; i++){
        if(i < sortedPlayers.length){
          top10Players.push(sortedPlayers[i]);
        }
      }

      let allTitlesFinalsValues = [];
      top10Players.forEach(function(d) {
          allTitlesFinalsValues.push(d.grandSlamTitles);
          allTitlesFinalsValues.push(d.grandslamFinals);
      });

      y.domain([0, top10Players[0].grandslamFinals*1.5]);

      let g = svg.append("g").attr("class", "y-axis-g");

      g.attr("transform",
          `translate(35,${-500})`)
          .transition()
          .duration(3000)
          .attr("transform", `translate(35,${-15})`);

      var yAxisTicks = y.ticks()
                        .filter(tick => Number.isInteger(tick));

      var yAxis = d3.axisLeft(y)
              .tickValues(yAxisTicks)
              .tickFormat(d3.format('d'));

      g.append("g")
          .attr("class", "axis axis--y")
          .call(yAxis);

      g = svg.append("g").attr("class", "axis y-axis-g-bC");

      g.attr("transform", `translate(35,1000)`)
          .transition()
          .duration(3000)
          .attr("transform", `translate(35,${margin.top + height / 2 + 35})`);

      // Setup bargram
      top10Players.forEach(function (d, i) {
          let tempArr = [];
          let prize = [];
          tempArr.push({"name": d.name + "1", "value": d.grandSlamTitles});
          tempArr.push({"name": d.name + "2", "value": d.grandslamFinals});

          // scale the range of the data
          x.domain(tempArr.map(d => d.name));

          var g = svg.append("g")
              .attr("transform",
                  `translate(${margin.left * 2 * i + 83},${-15})`);

          var bar = g.selectAll(".bar")
              .data(tempArr)
              .enter().append("rect")
              .attr("class", "bar")
              .attr("id", "bar"+ i.toString())
              .attr("x", function (d) {
                  return x(d.name);
              })
              .attr("y", height/2)
              .attr("height", 0)
              .attr("width", 3)
              .attr("fill", function(d) {
                  return color(d.name);
              })
              .on("mouseover", function (d, i) {
                  divTooltip.style("opacity", 1);
                  if (i===0) {
                      divTooltip.html(`<span>${d.name.slice(0, -1)}: <span/><br/><span>Number of titles: ${d.value}</span><br/>`)
                          .style("top", `${d3.event.pageY - 50}px`);
                  } else {
                      divTooltip.html(`<span>${d.name.slice(0, -1)}: <span/><br/><span>Number of finals: ${d.value}</span><br/>`)
                          .style("top", `${d3.event.pageY - 50}px`);
                  }

              }).on("mouseout", function (){
                  divTooltip.style("opacity", 0);
              })
              .on("mousemove", function() {
                  divTooltip.style("left", `${d3.event.pageX}px`)
                      .style("top", `${d3.event.pageY - 90}px`);
              });

          bar.transition()
              .duration(3000)
              .attr("y", function (d) {
                  return y(d.value);
              })
              .attr("height", function (d) {
                  return height/2 - y(d.value);
              });

          let circlesOnBars = g.selectAll(".circle")
              .data(tempArr)
              .enter().append("circle")
              .attr("class", "circle")
              .attr("id", "circle" + i.toString())
              .attr("cx", function (d) {
                  return x(d.name) + 1.5;
              })
              .attr("cy", -30)
              .on("mouseover", function (d, i) {
                  divTooltip.style("opacity", 1);
                  if (i == 0) {
                      divTooltip.html(`<span>${d.name.slice(0, -1)}: <span/><br/><span>Number of titles: ${d.value}</span><br/>`)
                          .style("top", `${d3.event.pageY - 50}px`);
                  } else {
                      divTooltip.html(`<span>${d.name.slice(0, -1)}: <span/><br/><span>Number of finals: ${d.value}</span><br/>`)
                          .style("top", `${d3.event.pageY - 50}px`);
                  }

              })
              .on("mouseout", function () {
                  divTooltip.style("opacity", 0);
              })
              .on("mousemove", function () {
                  divTooltip.style("left", `${d3.event.pageX}px`)
                      .style("top", `${d3.event.pageY - 50}px`);
              });

          circlesOnBars.transition()
              .duration(3000)
              .attr("cy", function (d) {
                  return y(d.value);
              })
              .attr("r", 7)
              .attr("fill", function(d) {
                  return color(d.name);
              });

          let gNames = g.append("g")
              .attr("class", "names")
              .attr("id", "name" + i.toString())
              .on("mouseover", function () {
                  divTooltip.style("opacity", 1);
                  divTooltip.html(`<span>${d.name}: <span/><br/><span>Number of titles: ${d.grandSlamTitles}</span><br/><span>Number of finals: ${d.grandslamFinals}</span><br/>`)
                      .style("top", `${d3.event.pageY - 50}px`)
                  d3.select(this).style("cursor", "pointer");
              })
              .on("mouseout", function () {
                  divTooltip.style("opacity", 0);
                  d3.select(this).style("cursor", "default");
              })
              .on("mousemove", function () {
                  divTooltip.style("left", `${d3.event.pageX}px`)
                      .style("top", `${d3.event.pageY - 90}px`);
              })
              .on("click", function(){
                updateConnectedScatterPlot(value, period, d.name);
                d3.selectAll(".bar").attr("opacity", 0.3);
                d3.selectAll(".circle").attr("opacity", 0.3);
                d3.selectAll("#bar" + i.toString()).attr("opacity", 1);
                d3.selectAll("#circle" + i.toString()).attr("opacity", 1);
              });

          let name = gNames.append("text")
              .attr("y", height / 2 + margin.top + 28)
              .attr("x", function () {
                  if (d.name.split(" ")[0].length < 4) {
                      return 0;
                  } else if (d.name.split(" ")[0].length < 5) {
                      return -7;
                  } else if (d.name.split(" ")[0].length < 6) {
                      return -9;
                  } else if (d.name.split(" ")[0].length < 7) {
                      return -10;
                  } else if (d.name.split(" ")[0].length < 8) {
                      return -14;
                  } else {
                      return -16;
                  }
              })
              .text(function () {
                  return d.name.split(" ")[0];
              })
              .attr("font-size", 20)
              .style("fill", "#ffffff");

          name.attr("opacity", 0).transition().duration(1000).attr("opacity", 1);

          let surname = gNames.append("text")
              .attr("y", height / 2 + margin.top + 50)
              .attr("x", function () {
                  if (d.name.split(" ")[1].length < 4) {
                      return 2;
                  } else if (d.name.split(" ")[1].length < 5) {
                      return -1;
                  } else if (d.name.split(" ")[1].length < 6) {
                      return -8;
                  } else if (d.name.split(" ")[1].length < 7) {
                      return -13;
                  } else if (d.name.split(" ")[1].length < 8) {
                      return -14;
                  } else {
                      return -19;
                  }
              })
              .text(function () {
                  return d.name.split(" ")[1];
              })
              .attr("font-size", 20)
              .style("fill", "#ffffff");

          surname.attr("opacity", 0).transition().duration(1000).attr("opacity", 1);
        });
    }
}


function drawLegendLineCircleChart(svgLegend, width) {
    svgLegend.append("rect")
        .attr("x", width-170)
        .attr("height", 50)
        .attr("width", 3)
        .attr("y", -90)
        .transition()
        .duration(1000)
        .attr("y", 30)
        .attr("fill", "#e6b800");

    svgLegend.append("circle")
        .attr("cx", width-168.5)
        .attr("fill", "#e6b800")
        .attr("r", 7)
        .attr("cy", -150)
        .transition()
        .duration(1000)
        .attr("cy", 26);

    svgLegend.append("text")
        .attr("x", width - 155)
        .text("titles")
        .attr("fill", "#b1c7e2")
        .attr("font-size", 17)
        .attr("y", 60)
        .attr("opacity", 0)
        .transition()
        .duration(1000)
        .attr("opacity", 1);

    svgLegend.append("rect")
        .attr("height", 50)
        .attr("width", 3)
        .attr("x", width - 84.5)
        .attr("fill", "#b30000")
        .attr("y", -90)
        .transition()
        .duration(1000)
        .attr("y", 30);

    svgLegend.append("circle")
        .attr("cx", width-82.5)
        .attr("fill", "#b30000")
        .attr("r", 7)
        .attr("cy", -150)
        .transition()
        .duration(1000)
        .attr("cy", 26);

    svgLegend.append("text")
        .attr("x", width - 70)
        .attr("y", 60)
        .text("finals")
        .attr("fill", "#b1c7e2")
        .attr("font-size", 17)
        .attr("opacity", 0)
        .transition()
        .duration(1000)
        .attr("opacity", 1);
}
