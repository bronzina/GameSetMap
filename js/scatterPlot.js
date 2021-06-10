var genderScatter = "atp";
var periodScatter = "all";
var colorGroup = [ "#6666ff", "#993300", "#009900", "#949109"];
//var colorscale = d3.scaleOrdinal(d3.schemeCategory10);

var colorscale = d3.scaleOrdinal(["#3300FF", "#FF6600", "#FFCC00", "#FF66CC", "#00CCFF"]);


function drawScatterPlot(gender, period, player){

    genderScatter = gender;
    periodScatter = period;


    let svg1 = d3.select(".statisticsDiv").append("div").attr("class", "scatterText").attr("position", "absolute")
                  .attr("width", 100)
                  .attr("height", 300);

  svg1.append("text")
    .attr("class", "scatterDescription")
    .text("The scatter plot is the representation of 6 percentage statistics ")
    .attr("fill", "#748293")
    .attr("font-size", "0.9em");

    svg1.append("text")
      .attr("class", "scatterDescription")
      .text("(ace %, double faults %, 1st won points %, 2nd won points %,")
      .attr("fill", "#748293")
      .attr("font-size", "0.9em");

    let svg2 = d3.select(".statisticsDiv").append("div").attr("class", "scatterText").attr("position", "absolute")
                .attr("width", 100)
                .attr("height", 300);

    svg2.append("text")
      .attr("class", "scatterDescription")
      .text("break points saved %, break points won %) ")
      .attr("fill", "#748293")
      .attr("font-size", "0.9em");

    svg2.append("text")
      .attr("class", "scatterDescription")
      .text("using PCA technique for representation on two principal components.")
      .attr("fill", "#748293")
      .attr("font-size", "0.9em");

      let svg3 = d3.select(".statisticsDiv").append("div").attr("class", "scatterText").attr("position", "absolute")
                  .attr("width", 100)
                  .attr("height", 300);

      svg3.append("text")
          .attr("class", "scatterDescription")
          .text("Click on dots or search for players to show statistics on radar chart!")
          .attr("fill", "#748293")
          .attr("font-size", "0.9em");

  let margin = {top: 0, right: 20, bottom: 20, left: 0},
      width = 950 - margin.left - margin.right,
      height = 500 - margin.top - margin.bottom;


    let svg = d3.select(".statisticsDiv")
        .append("svg").attr("class", "scatterPlot")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .attr('transform', 'translate(-100,0)');

  svg.attr("opacity",0).transition().duration(100).attr("opacity",1);

  var LegendOptions = ["Hard", "Clay", "Grass", "No comparable surface"]

  var s = d3.select(".statisticsDiv")
    .append("svg")
    .attr("id", "scatterLegend")
    .attr("width", 300)
    .attr("height", 150)
     .attr("transform", "translate(-1200, 0)")
     .style("position", "absolute")
     .style("float", "bottom");

  var legend = s.append("g")
    .attr("class", "legend")
    .attr("height", 100)
    .attr("width", 200);

  legend.selectAll('rect')
     .data(LegendOptions)
     .enter()
     .append("rect")
     .attr("x", 30)
     .attr("y", function(d, i){ return i * 20+35;})
     .attr("width", 15)
     .attr("height", 15)
     .style("fill", function(d, i){ return colorGroup[i]; });

  legend.selectAll('text')
   	  .data(LegendOptions)
   	  .enter()
   	  .append("text")
      .attr("id", function(d, i){
        return "text" + i.toString();
      })
   	  .attr("x", 50)
   	  .attr("y", function(d, i){ return i * 20 + 48;})
   	  .attr("font-size", "15px")
   	  .attr("fill", "#ffffff")
   	  .text(function(d) { return d; });

  // Open PCA data file
  d3.csv("../data/preprocessed/radar/" + genderScatter + "_dataFullPCA_"+ periodScatter + ".csv", function(error, data) {
    if (error) throw error;

    // Cast my values as numbers and determine ranges.
    var minmax = {Y1: {min:0, max:0}, Y2: {min:0, max:0}}
    data.forEach(function(d) {
      d.Y1 = + parseFloat(d.Y1);
      d.Y2= + parseFloat(d.Y2);
      minmax.Y1.min = Math.min(d.Y1, minmax.Y1.min);
      minmax.Y1.max = Math.max(d.Y1, minmax.Y1.max);
      minmax.Y2.min = Math.min(d.Y2, minmax.Y2.min);
      minmax.Y2.max = Math.max(d.Y2, minmax.Y2.max);
    });

    // Set-up my x scale.
    var x = d3.scaleLinear()
      .range([0, width])
      .domain([Math.floor(minmax.Y1.min), Math.ceil(minmax.Y1.max)]);

  // Set-up my y scale.
  var y = d3.scaleLinear()
    .range([height, 0])
    .domain([Math.floor(minmax.Y2.min), Math.ceil(minmax.Y2.max)]);

  // Create my x-axis using my scale.
  var xAxis = d3.axisBottom()
    .scale(x);

  // Create my y-axis using my scale.
  var yAxis = d3.axisLeft()
    .scale(y);


  // Create my tooltip creating function.
  var tip = d3.tip()
    .attr('class', 'd3-tip')
    .offset([-10, 0])
    .html(function(d) {
      return "<strong style=" + "color: #b1c7e2>" + d.name;
    });

  // Initialize my tooltip.
  svg.call(tip);

  // Draw my x-axis.
  svg.append("g")
    .attr("class", "x")
    .attr("transform", "translate(0," + y(0) + ")")
    .call(xAxis)
  .append("text")
    .attr("class", "label")
    .attr("x", width)
    .attr("y", -6)
    .style("text-anchor", "end")
    .style("fill", "#748293")
    .text("Component 1");

  // Draw my y-axis.
  svg.append("g")
    .attr("class", "y")
    .attr("transform", "translate(" + x(0) + ",10)")
    .call(yAxis)
  .append("text")
    .attr("class", "label")
    .attr("transform", "rotate(-90)")
    .attr("y", 6)
    .attr("dy", ".71em")
    .style("text-anchor", "end")
    .style("fill", "#748293")
    .text("Component 2");

    //Brushing
    var brush = d3.brush().extent([[0, 0], [width, height]]).on("end", brushended),
          idleTimeout,
          idleDelay = 350;

    svg.append("g")
        .attr("class", "brush")
        .call(brush);

    function brushended() {
          var s = d3.event.selection;
          if (!s) {
              if (!idleTimeout) return idleTimeout = setTimeout(idled, idleDelay);
              x.domain(d3.extent(data, function (d) { return d.Y1; })).nice();
              y.domain(d3.extent(data, function (d) { return d.Y2; })).nice();
          } else {
              x.domain([s[0][0], s[1][0]].map(x.invert, x));
              y.domain([s[1][1], s[0][1]].map(y.invert, y));
              svg.select(".brush").call(brush.move, null);
          }
          zoom();
      }

      function idled() {
            idleTimeout = null;
        }

      function zoom() {
        var t = svg.transition().duration(750);
        svg.select(".x").transition(t).call(xAxis);
        svg.select(".y").transition(t).call(yAxis);
        svg.selectAll("circle").transition(t)
           .attr("cx", function (d) {
             return x(d.Y1);
           })
           .attr("cy", function (d) {
              return y(d.Y2);
            });
        }

  // Create all the data points
  var points = svg.selectAll(".dot")
    .data(data)
  .enter().append("circle")
    .attr("class", "dot")
    .attr("r", function(d){
      if(d.name == player){
        return 10;
      }
      else{
        return 3.5;
      }
    })
    .attr("cx", function(d) { return x(d.Y1); })
    .attr("cy", function(d) { return y(d.Y2); })
    .style("fill", function(d){
      if(d.name == player){
        d3.select(this).raise();
        //return "#990000";
        return colorscale[i];
      }
      else{
        return "#949109";
      }
    })
    .on('mouseover', tip.show)
    .on('mouseout', tip.hide)
    .on('click', function(d){
      updateScatterPlotSearch(d.name);
      searchFor(d.name);
    });

  });

}

function prepareDataRadar(d){
  if(selections.length >= 5){
    selections = [];
    actual = [];
  }
  if(actual.includes(d.name)){
    updateRadarChart(selections);
  }
  else{
    actual.push(d.name);
    selections.push(d);
    updateRadarChart(selections);
  }
}

function searchFor(player){
  d3.csv("../data/preprocessed/radar/" + genderScatter + "_dataFullPCA_"+ periodScatter + ".csv", function(error, data) {
    if (error) throw error;
    data.forEach(function(d){
      if(d.name == player){
        prepareDataRadar(d);
      }
    });
  });
}

var selections = [];
var actual = [];

function updateScatterPlot(gender, period){
  removeScatter();
  d3.select(".mainWrapper").append("div").attr("class", "statisticsDiv").attr("height", 1200).attr("width", 1400);
  searchBar(gender);
  genderScatter = gender;
  periodScatter = period;
  drawScatterPlot(genderScatter, periodScatter, "");
  selections = [];
  updateRadarChart([]);
}

var i = 0;

function updateScatterPlotSearch(player){

  var players = [];
  var p = {};
  var hardPlayers = [];
  var clayPlayers = [];
  var grassPlayers = [];
  var nothingPlayers = [];

  d3.csv("../data/preprocessed/pca/" + genderScatter +"_players_statistics_" + periodScatter + ".csv", function(error, dataGroup){
    dataGroup.forEach(function(d){
      players.push(d);
      if(d.name == player){
        p = d;
      }
    });

    setTimeout(function(){
      players.forEach(function(d){
        var hard = parseInt(p.hard);
        var clay = parseInt(p.clay);
        var grass = parseInt(p.grass);
        var hardNeighbour = parseInt(d.hard);
        var clayNeighbour = parseInt(d.clay);
        var grassNeighbour = parseInt(d.grass);
        var hardDiff;
        if(hard >= hardNeighbour){
          hardDiff = hard - hardNeighbour;
        }
        else{
          hardDiff = hardNeighbour - hard;
        }
        var clayDiff;
        if(clay >= clayNeighbour){
          clayDiff = clay - clayNeighbour;
        }
        else{
          clayDiff = clayNeighbour - clay;
        }
        var grassDiff;
        if(grass >= grassNeighbour){
          grassDiff = grass - grassNeighbour;
        }
        else{
          grassDiff = grassNeighbour - grass;
        }

        var similar = Math.min(hardDiff, clayDiff, grassDiff);

        if(similar == hardDiff){
          var percent = (50 * hard) / 100;
        }
        else if(similar == clayDiff){
          var percent = (50 * clay) / 100;
        }
        else{
          var percent = (50 * grass) / 100;
        }

        if(((hardNeighbour > hard + percent) || (hardNeighbour < hard - percent)) &&  ((clayNeighbour > clay + percent) || (clayNeighbour < clay - percent))
                  &&  ((grassNeighbour > grass + percent) || (grassNeighbour < grass - percent)) ){
                    nothingPlayers.push(d.name);
        }

        else{

          if(similar == hardDiff){
            if((similar <= hard+percent) || (similar >= hard-percent)){
              hardPlayers.push(d.name);
            }
          }
          else if(similar == clayDiff){
            if((similar <= clay+percent) || (similar >= clay-percent)){
              clayPlayers.push(d.name);
            }
          }
          else if(similar == grassDiff){
            if((similar <= grass+percent) || (similar >= grass-percent)){
              grassPlayers.push(d.name);
            }
          }
        }
      });

      var name;

      d3.selectAll(".dot").each(function(){
        d3.select(this)
          .transition()
          .duration(200)
          .style("fill", function(d){
            var name = d.name;
            if(hardPlayers.includes(name)){
              return colorGroup[0];
            }
            else if(clayPlayers.includes(name)){
              return colorGroup[1];
            }
            else if(grassPlayers.includes(name)){
              return colorGroup[2];
            }
            else{
              return colorGroup[3];
            }
          })
          .attr("r", 3.5)
          .style("stroke", "none")
          .attr("fill-opacity", function(d){
            name = d.name;
            if(hardPlayers.includes(name)){
              return 1.0;
            }
            else if(clayPlayers.includes(name)){
              return 1.0;
            }
            else if(grassPlayers.includes(name)){
              return 1.0;
            }
            else{
              return 0.2;
            }
          });
          if(hardPlayers.includes(name)){
            d3.select(this).raise();
          }
          else if(clayPlayers.includes(name)){
            d3.select(this).raise();
          }
          else if(grassPlayers.includes(name)){
            d3.select(this).raise();
          }
      });
      d3.selectAll(".dot").each(function(d){
        if(d.name == player){
          d3.select(this).transition()
            .duration(200)
            //.style("fill", "#990000")
            .style("fill", function(){
              i = i+1;
              if(i == 5){
                i = 0;
              }
              return colorscale(i-2);
            })
            .style("fill-opacity", 1)
            .attr("r", 10)
            .style("stroke", "white");
          d3.select(this).raise();
        }
      });
    }, 10);
  });
}


function removeScatter(){
  d3.select(".statisticsDiv").remove();
}
