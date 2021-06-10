atp_year = {
  "atpall": "preprocessed/map/atp_players_with_rank_all-time.csv",
  "atp2021": "preprocessed/map/atp_players_with_rank.csv",
  "atp2020": "preprocessed/map/atp_players_with_rank_20s.csv",
  "atp2010": "preprocessed/map/atp_players_with_rank_10s.csv",
  "atp2000": "preprocessed/map/atp_players_with_rank_00s.csv",
  "atp1990": "preprocessed/map/atp_players_with_rank_90s.csv",
  "atp1980": "preprocessed/map/atp_players_with_rank_80s.csv"
}

wta_year = {
  "wtaall": "preprocessed/map/wta_players_with_rank_all-time.csv",
  "wta2021": "preprocessed/map/wta_players_with_rank.csv",
  "wta2020": "preprocessed/map/wta_players_with_rank_20s.csv",
  "wta2010": "preprocessed/map/wta_players_with_rank_10s.csv",
  "wta2000": "preprocessed/map/wta_players_with_rank_00s.csv",
  "wta1990": "preprocessed/map/wta_players_with_rank_90s.csv",
  "wta1980": "preprocessed/map/wta_players_with_rank_80s.csv"
}



//const colorScheme = ["#cfd3d6", "#efee6a", "#93c96e", "#54a977", "#278074", "#215860", "#243644"];
//colorScheme.unshift("#cfd3d6");

const colorScheme = ["#cfd3d6", "#d9f0a3", "#addd8e", "#78c679", "#41ab5d", "#238443", "#005a32"];
colorScheme.unshift("#cfd3d6");

var genderMap = "atp";
var periodMap = "2021";


function compareNumeric(a, b) {
    if (a > b) return 1;
    if (a < b) return -1;
}

//Initially, gender = atp and iter = 0
function drawMap(gender, period, iter) {
    // svg

    let svg = d3.select(".mainWrapper").append("div")
                .attr("class", "countryDiv")
                .attr("width", 1400)
                .attr("height", 800)
                .style("position", "absolute");


    let svg1 = d3.select(".countryDiv").append("div")
                .attr("class", "playersDiv")
                .attr("id", "country")
                .attr("width", 50)
                .attr("height", 50)
                .attr("position", "absolute")
                .style("float", "left")
                .append("text")
                .attr("id", "countryText")
                .text("Click on a country to show its players!")
                .style("left", "0px");


    let svg2 = d3.select(".countryDiv").append("div")
          .attr("class", "map")
          .append("svg")
          .attr("width", 1250)
          .attr("height", 600)
          .style("position", "absolute")
          .style("margin", "auto")
          .style("float", "right");

    width = +svg2.attr("width"),
    height = +svg2.attr("height");

    if(iter === 0) {
      svg2.attr("opacity", 0).transition().duration(3000).attr("opacity", 1);
    }

    let projection = d3.geoNaturalEarth()
        .scale(width / 2 / Math.PI)
        .translate([width / 2, 390]);
    let path = d3.geoPath()
        .projection(projection);

    let divTooltip = d3.select("body").append("div")
        .attr("class", "tooltip")
        .style("opacity", 0);


      // Data and color scale
    let data = {};

    if(gender == "atp"){
      d3.queue()
          .defer(d3.json, "data/world-110m.json")
          .defer(d3.csv, "data/" + atp_year["atp" + period])
          .await(ready);
    }
    else{
      d3.queue()
          .defer(d3.json, "data/world-110m.json")
          .defer(d3.csv, "data/" + wta_year["wta" + period])
          .await(ready);
    }

    function ready(error, topo, dataTennis) {
        if (error) throw error;
        let countValues = [];
        let top100players = [];
        dataTennis.forEach(function(row) {
            data[row.country] = {"players": row.n_players};
            players[row.country] = {"players": row.players};
            countValues.push(row.n_players);
        });


        let legendValues = getIntervalsForLegend(countValues, gender, period);
        let legendInterval = legendValues[0];
        let legendLabels = legendValues[1];

        let colorScale = d3.scaleThreshold()
            .domain(legendInterval)
            .range(colorScheme);

        let reversedLegendInterval = legendInterval.reverse();
        let reversedLegendLabels = legendLabels.reverse();

        let legend = svg2.selectAll("g.legend")
            .data(reversedLegendInterval)
            .enter().append("g")
            .attr("class", "legend");

        const ls_w = 55, ls_h = 15;
        legend.append("rect")
            .attr("x", function(d, i){ return width/1.58 - (i*ls_w);})
            .attr("y", 0)
            .attr("width", ls_w)
            .attr("height", ls_h)
            .style("fill", function(d) { return colorScale(d); })
            .style("opacity", 0.96)
            .attr("stroke", "white")
            .attr("stroke-width", 0.5);

        legend.append("text")
            .attr("class","textRect")
            .attr("x", function(d, i){
                if (i === reversedLegendInterval.length-1) {
                    return width/1.53 - (i*ls_w);
                } else if (i === 0) {
                    return width/1.55 - (i*ls_w)
                } else if (i === reversedLegendInterval.length-2) {
                    return width/1.555 - (i*ls_w);
                } else {
                    return width/1.57 - (i*ls_w);
                }
            })
            .attr("y", 30)
            .text(function(d, i){ return reversedLegendLabels[i]; })
            .attr("fill", "white")
            .attr("font-size", "0.9em");

        svg2.append("text")
            .attr("class","textTooltip")
            .attr("y", 55)
            .attr("x", width/2 - ls_w*3)
            .text("*hover over the country to see the number of players")
            .attr("fill", "#748293")
            .attr("font-size", "0.9em");

        let countries = svg2.append("g")
            .attr("class", "countries")
            .selectAll("path")
            .data(topo.features)
            .enter().append("path")
            .attr("class", "country")
            .attr("stroke", "white")
            .attr("stroke-width", 0.5)
            .attr("fill", function (d) {
                if (data[d.id]) {
                    d.n_players = data[d.id]["players"];
                } else {
                    d.n_players = 0;
                }
                return colorScale(d.n_players);
            })
            .attr("d", path);

        countries.attr("opacity", 0)
            .transition()
            .duration(200)
            .attr("opacity", 0.95);


        if (iter === 0) {
            var timeDurationClarification = 2300;
        } else {
            var timeDurationClarification = 1000;
        }

        var genderCap = gender.toUpperCase();

        svg2.append("text")
            .attr("class", "description")
            .attr("x", 900)
            .attr("y", 10)
            .text("The map represents the number of tennis players")
            .attr("fill", "#b1c7e2")
            .attr("font-size", 14);

        svg2.append("text")
            .attr("class", "description")
            .attr("id", "description")
            .attr("x", 910)
            .attr("y", 30)
            .text("of the top 100 in the " + genderCap + " ranking (" + period + ").")
            .attr("fill", "#b1c7e2")
            .attr("font-size", 14);


        countries.on("mouseover", function(d) {
            d3.select(this).style("cursor", "pointer");
            //d3.select(this).transition().duration(200).style("opacity", 1);
            divTooltip.transition().duration(200)
                .style("opacity", 0.95)
            divTooltip.html(`<span>Country: ${d.properties.name}<span/><br/><span/>Number of players: ${d.n_players}`)
                .style("left", `${d3.event.pageX}px`)
                .style("top", `${d3.event.pageY - 30}px`);
            })
            .on("mouseout", function() {
                /*d3.select(this)
                    .transition().duration(200)
                    .style("opacity", 0.95);*/
                divTooltip.transition().duration(200)
                    .style("opacity", 0);
            })
            .on("click", function(d){
              d3.selectAll(".country").transition().duration(500).attr("opacity", 0.5);
              d3.select(this).transition().duration(500).attr("opacity", 1);
              //d3.select(".body").on("click", function(){ d3.selectAll(".country").attr("opacity", 0.95); })
              var list = [];
                if (players[d.id]) {
                    d.players = players[d.id]["players"];
                } else {
                    d.players = [];
                }
                list = formListPlayers(d.players);

              d3.select("ol").remove();

              d3.select("#countryText")
                .text("Top 100 players coming from " + d.properties.name + ":");
                //.attr("transform", "translate(-50, 0)");

              var ol = d3.select(".playersDiv")
                  .append("ol")
                  .attr("x", -30);


              ol.selectAll("li")
                  .data(list)
                  .enter()
                  .append('li')
                  .html(String)
                  .style("fill", "#b1c7e2")
                  .on("mouseover", function(){
                    d3.select(this).style("cursor", "pointer");
                  })
                  .on("click", function(d){
                    statisticsFunction(this.innerHTML);
                    updateScatterPlotSearch(this.innerHTML);
                    searchFor(this.innerHTML);
                  });
            });
    }
}


function formListPlayers(list){
  var p = list.split(",");
  for(i=0; i < p.length; i++){
    p[i].toString();
    p[i] = p[i].substring(2, p[i].length-1);
  }
  p[p.length-1] = p[p.length-1].slice(0, -1);
  return p;
}

function getIntervalsForLegend(arr, gender, period){
    arr.sort(compareNumeric);
    if (gender === "atp") {
      if(period === "2021" || period == "2020"){
        var legendIntervals = [0, 1, 3, 5, 7, 9, 11];
      }
      else if(period == "all"){
        var legendIntervals = [0, 1, 20, 40, 60, 80, 100];
      }
      else{
        var legendIntervals = [0, 1, 5, 10, 15, 20, 25];
      }
    } else {
      if(period === "2021" || period == "2020"){
        var legendIntervals = [0, 1, 3, 5, 7, 9, 11];
      }
      else if(period == "all"){
        var legendIntervals = [0, 1, 20, 40, 60, 80, 100];
      }
      else{
        var legendIntervals = [0, 1, 5, 10, 15, 20, 25];
      }
    }

    let legendLabels = [legendIntervals[0]];
    legendIntervals.slice(1,legendIntervals.length-1).forEach(function(interval, i){
        legendLabels.push(interval+ "-" + String(legendIntervals[i+2]-1));
    });
    legendLabels.push(legendIntervals[legendIntervals.length-1] + " +");
    return [legendIntervals, legendLabels];
}

function updateGeneral(selGender, selPeriod){
  genderMap = selGender;
  periodMap = selPeriod;
  if(genderMap == "atp"){
    d3.queue()
      .defer(d3.csv, "data/" + atp_year["atp" + period])
      .await(readyForUpdate);
  }
  else{
    d3.queue()
        .defer(d3.csv, "data/" + wta_year["wta" + period])
        .await(readyForUpdate);
  }
  d3.selectAll(".country").transition().duration(500).attr("opacity", 0.95);
  d3.select("#countryText")
    .text("Click on a country to show its players!");
  d3.select("ol").remove();
}



function readyForUpdate(error, dataNew){
    if (error) throw error;

    let countValues = [];
    let data = {};
    dataNew.forEach(function(row) {
        data[row.country] = {"players": row.n_players};
        players[row.country] = {"players": row.players};
        countValues.push(row.n_players);
    });

    var formEl = document.forms.years;
    var formData = new FormData(formEl);
    period = formData.get('year');
    var formEl1 = document.forms.genderFormAtp;
    var formData1 = new FormData(formEl1);
    gender = formData1.get('gender');

    let legendValues = getIntervalsForLegend(countValues, gender, period);
    let legendInterval = legendValues[0];
    let legendLabels = legendValues[1];

    let colorScale = d3.scaleThreshold()
        .domain(legendInterval)
        .range(colorScheme);

    d3.selectAll('.country')
        .transition().duration(200)
        .attr('fill', function(d) {
            if(data[d.id]) {
                d.n_players = data[d.id]["players"];
            } else {
                d.n_players = 0;
            }
            return colorScale(d.n_players);
        });

    updateText(gender, period);

    let reversedLegendLabels = legendLabels.reverse();
    d3.selectAll("text.textRect")
        .attr("opacity", 0)
        .text(function(d, i){ return reversedLegendLabels[i]; })
        .transition().duration(200)
        .attr("opacity", 1)
}

function updateText(gender, period){
  var genderCap = gender.toUpperCase();
  if(period == "2021" || period == "2020"){
    d3.select('#description')
      .attr("x", 960)
      .text("of the top 100 in the " + genderCap + " ranking (" + period + ").");
  }
  else{
    var endPeriod = (parseInt(period) + 9).toString();
    d3.select('#description')
      .attr("x", 950)
      .text("of the top 100 in the " + genderCap + " ranking (" + period + "-" + endPeriod +").");
  }
}

window.onclick = function(event){
          if(!(event.target.className.baseVal=="country")){
              d3.selectAll('.country').transition().duration(500).attr('opacity', 0.95);
              d3.select("#countryText")
                .text("Click on a country to show its players!");
              d3.select("ol").remove();
            }
    }
