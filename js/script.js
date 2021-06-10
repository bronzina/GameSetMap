// Draw background
function drawTitlePageLayout(mainWrapper) {

    //Draw the pitch in the background
    let bgWrapper = d3.select("body").append("div").attr("class", "bgWrapper");
    bgWrapper.append("div").attr("class", "topHorizontalLine1");
    bgWrapper.append("div").attr("class", "topHorizontalLine2");
    bgWrapper.append("div").attr("class", "bottomHorizontalLine1");
    bgWrapper.append("div").attr("class", "bottomHorizontalLine2");
    bgWrapper.append("div").attr("class", "leftVerticalLine1");
    bgWrapper.append("div").attr("class", "middleVerticalLine1");
    bgWrapper.append("div").attr("class", "rightVerticalLine1");
    bgWrapper.append("div").attr("class", "middleHorizontalLine1");
    bgWrapper.append("div").attr("class", "leftVerticalLine2");
    bgWrapper.append("div").attr("class", "rightVerticalLine2");

    //Draw the title
    let indexTitle = mainWrapper.append("div").attr("class", "indexTitle");
    indexTitle.append("span").html("Game");
    indexTitle.append("span").html("Set");
    indexTitle.append("span").html("Map");

    //Draw the  buttons
    let buttonsCharts = mainWrapper.append("div").attr("class", "buttonsCharts");

    //Map button
    let mapBtn = buttonsCharts.append("div").attr("class", "mapButton btn");
    mapBtn.append("svg").attr("class", "mapButtonSvg").attr("height", 160).attr("width", 200);
    mapBtn.append("span").html("Tennis players around the world");
    mapBtn.append("div").attr("class", "buttonLine").append("div");

    //Line chart button
    let statisticsChartBtn = buttonsCharts.append("div").attr("class", "statisticsChartButton btn");
    statisticsChartBtn.append("svg").attr("class", "statisticsChartButtonSvg").attr("height", 160).attr("width", 200);
    statisticsChartBtn.append("span").html("Players statistics");
    statisticsChartBtn.append("div").attr("class", "buttonLine").append("div");

    //Bar chart button
    let barChartBtn = buttonsCharts.append("div").attr("class", "barChartButton btn");
    barChartBtn.append("svg").attr("class", "barChartButtonSvg").attr("height", 160).attr("width", 200);
    barChartBtn.append("span").html("Career achievements");
    // barChartBtn.append("span").attr("class","span2").html("records");
    barChartBtn.append("div").attr("class", "buttonLine").append("div");


    let footer = mainWrapper.append("div").attr("class", "footer");

    let sources = footer.append("div").attr("class","sources footerDivLeft").append("ul");
    sources.append("li").html("Data sources:");
    sources.append("li").html("Repository of tennis data of ").append("a").attr("href", "https://github.com/JeffSackmann").html("Jeff Sackmann");

    let author = footer.append("div").attr("class","author footerDivRight");
    author.append("span").html("Author:");
    author.append("span").html("Andrea Luca Antonini");
}

//Draw buttons on the main page
function drawInitialButtons() {
    //svg for logo for buttons
    let svgMapButton = d3.select("svg.mapButtonSvg")
            .attr("width", 200),
        widthMapButton = +svgMapButton.attr("width");

    let svgLineButton = d3.select("svg.statisticsChartButtonSvg")
            .attr("width", 200),
        widthLineButton = +svgLineButton.attr("width"),
        heightLineButton = +svgLineButton.attr("height");

    let svgBarChartButton = d3.select("svg.barChartButtonSvg")
            .attr("width", 200),
        widthBarChartButton = +svgBarChartButton.attr("width"),
        heightBarChartButton = +svgBarChartButton.attr("height");

    //data for line Chart
    let dataLineButton = [1, 5, 4, 5, 5, 7, 9.8, 6, 9, 7, 5].reverse();
    let dataLineButton2 = [0, 4, 2, 3, 2, 6, 7, 5, 7, 6, 4].reverse();

    //data for bar Chart
    let barChartButtonData = [4, 8, 15, 16, 23, 42].reverse();

    //x y for line Chart
    let xLineButton = d3.scaleLinear().domain([0, 10]).range([0, widthLineButton]);
    let yLineButton = d3.scaleLinear().domain([0, 10]).range([50, heightLineButton]);

    //x y for bar Chart
    let xBarChartButton;
    xBarChartButton = d3.scaleBand()
        .domain([0, 1, 2, 3, 4, 5])
        .range([0, widthBarChartButton])
        .padding(0.001);

    let yBarChartButton = d3.scaleLinear()
        .domain([0, 42])
        .range([heightBarChartButton, 70]);

    //line for line Chart
    let line = d3.line()
        .curve(d3.curveCardinal)
        .x(function (d, i) {
            return xLineButton(i);
        })
        .y(function (d) {
            return yLineButton(d);
        });

    //projection for map
    let projection = d3.geoNaturalEarth()
        .scale(widthMapButton / 1.52 / Math.PI)
        .translate([105, 115]);
    let path = d3.geoPath()
        .projection(projection);

    d3.queue()
        .defer(d3.json, "data/world-110m.json")
        .await(ready);

    function ready(error, topo) {
        if (error) throw error;
        //draw map for button on title page
        drawMapInitial(topo, svgMapButton, path);

        //draw line chart for button on title page
        drawStatisticsChart(svgLineButton, heightLineButton, xLineButton, yLineButton, line, dataLineButton, dataLineButton2);

        //draw bar chart for button on title page
        drawBarChart(svgBarChartButton, barChartButtonData, xBarChartButton, yBarChartButton, heightBarChartButton);

    }
}

function drawMapInitial(topo, svg, path) {
    let countries = svg.append("g")
        .attr("class", "countriesButton")
        .selectAll("path")
        .data(topo.features)
        .enter().append("path")
        .attr("class", "countryButton")
        .attr("stroke", "white")
        .attr("stroke-width", 0.5)
        .attr("fill", "#6886aa")
        .attr("d", path);

    countries.attr("opacity", 0)
        .transition()
        .duration(200)
        .attr("opacity", 0.35);
}

function drawStatisticsChart(svg, height, x,  y, line, data1, data2) {

    d3.selectAll(".statisticsChartButtonSvg .tick line").attr("x2", "-3");

    let pathStatisticsChart = svg.append("path")
        .attr("d", line(data1))
        .attr("stroke", "#6886aa")
        .attr("opacity", 0.35)
        .attr("stroke-width", "2")
        .attr("fill", "none");

    let totalLength = pathStatisticsChart.node().getTotalLength();

    pathStatisticsChart
        .attr("stroke-dasharray", `${totalLength} ${totalLength}`)
        .attr("stroke-dashoffset", totalLength)
        .transition()
        .duration(200)
        .attr("stroke-dashoffset", 0);


    let pathStatisticsChart2 = svg.append("path")
        .attr("d", line(data2))
        .attr("stroke", "#6886aa")
        .attr("opacity", 0.35)
        .attr("stroke-width", "2")
        .attr("fill", "none");

    totalLength = pathStatisticsChart2.node().getTotalLength();

    pathStatisticsChart2
        .attr("stroke-dasharray", `${totalLength} ${totalLength}`)
        .attr("stroke-dashoffset", totalLength)
        .transition()
        .duration(200)
        .attr("stroke-dashoffset", 0);
}

function drawBarChart(svg, data, x, y, height) {
    svg.append("g")
        .selectAll("rect")
        .data(data)
        .enter().append("rect")
        .attr("width", 25)
        .attr("x",function(d,i) { return x(i); })
        .attr("y",height)
        .attr("height", 0)
        .attr("stroke", "white")
        .attr("stroke-width", 0.9)
        .attr("fill", "#6886aa")
        .attr("opacity", 0.35)
        .transition()
        .duration(200)
        .attr("y",function(d) { return y(d); })
        .attr("height",function(d) { return height - y(d); })
        .on("end", function() {
            addEventsTitlePage();
        });
}

//Add events on the main page
function addEventsTitlePage() {
    d3.selectAll(".buttonsCharts div")
        .on("mouseover", function() {
            d3.select(this).style("cursor", "pointer");
            let selectedElement = d3.select(this).selectAll("span");
            let selectedElementClass = d3.select(this)
                .attr("class")
                .split(" ")[0];

            if (selectedElementClass === "mapButton") {
                d3.select(".countriesButton path")
                    .attr("opacity", 0.8)
                    .attr("stroke-width", 0.9);
            } else if (selectedElementClass === "statisticsChartButton") {
                d3.selectAll(".statisticsChartButton path")
                  .attr("opacity", "1")
                  .attr("color", "#9cc1ed");
            } else {
                d3.selectAll(".barChartButton rect")
                  .attr("opacity", 0.8)
                  .attr("stroke-width", "1.3");
            }
            selectedElement
                .style("font-weight", "bold")
                .style("color", "white");
        })
        .on("mouseout", function() {
            let selectedElementClass = d3.select(this).attr("class");
            if (selectedElementClass.split(" ")[0] === "mapButton") {
                d3.select(".countriesButton path")
                    .attr("opacity", 0.35)
                    .attr("stroke-width", 0.5);
            } else if (selectedElementClass.split(" ")[0] === "statisticsChartButton") {
                d3.selectAll(".statisticsChartButton path")
                    .attr("opacity", "0.35")
                    .attr("color", "#6886aa");
            } else {
                d3.selectAll(".barChartButton rect")
                  .attr("opacity", "0.35")
                  .attr("stroke-width", "0.9");
            }
            d3.select(this).selectAll("span")
                .style("font-weight", "normal")
                .style("color", "#cbdbed");
        })
        .on("click", function() {
            let selectedElementClass = d3.select(this).attr("class");

            d3.select("div."+selectedElementClass.split(" ")[0]+"Header span")
                .style("font-weight", "bold")
                .style("color", "white");

            d3.select("div."+selectedElementClass.split(" ")[0] + "Header .buttonLineHeader div")
                .style("height", "3px");
            removeTitlePageLayout(selectedElementClass.split(" ")[0]);
        })
}

//Remove main page
function removeTitlePageLayout(typeChart) {
    d3.select(".bgWrapper").remove();
    d3.select(".mainWrapper")
        .attr("opacity", 1)
        .transition()
        .duration(900)
        .style("top", "-120%")
        .attr("opacity", 0)
        .remove()
        .on("end", function() {
            d3.select("body").append("div").attr("class", "mainWrapper");
            drawHeader(typeChart);
        });
}


function drawHeader(typeChart) {
    let mainWrapper = d3.select(".mainWrapper");
    let buttonsChartsHeader = mainWrapper.append("div").attr("class", "buttonsChartsHeader");
    buttonsChartsHeader.attr("opacity", 0)
        .transition()
        .duration(800)
        .attr("opacity", 1);

    let mapBtnHeader = buttonsChartsHeader.append("div").attr("class", "mapButtonHeader btn");
    mapBtnHeader.append("span").html("Tennis players around the world");
    mapBtnHeader.append("div").attr("class", "buttonLineHeader").append("div");


    let statisticsChartBtnHeader = buttonsChartsHeader.append("div").attr("class", "statisticsChartButtonHeader btn");
    statisticsChartBtnHeader.append("span").html("Players statistics");
    statisticsChartBtnHeader.append("div").attr("class", "buttonLineHeader").append("div");


    let barChartBtnHeader = buttonsChartsHeader.append("div").attr("class", "barChartButtonHeader btn");
    barChartBtnHeader.append("span").html("Career achievements");
    barChartBtnHeader.append("div").attr("class", "buttonLineHeader").append("div");

    d3.selectAll(".buttonsChartsHeader div")
        .on("mouseover", function () {
            d3.select(this).style("cursor", "pointer");
        })
        .on("click", function() {
            var selectedElementClass = d3.select(this).attr("class");

            d3.selectAll(".buttonsChartsHeader span")
                .style("font-weight", "normal");

            d3.select("div."+selectedElementClass.split(" ")[0]+" span")
                .style("font-weight", "bold")
                .style("color", "white");

            d3.selectAll(".buttonsChartsHeader .buttonLineHeader div")
                .style("height", "2px");

            d3.select("div."+selectedElementClass.split(" ")[0] + " .buttonLineHeader div")
                .style("height", "3px");
            if (selectedElementClass.split(" ")[0] === "mapButtonHeader") {
                removeSvg();
                d3.select(".main-nav")
                  .style("opacity", 1);
                d3.selectAll(".tooltip").remove();
                var formEl = document.forms.years;
                var formData = new FormData(formEl);
                var periodMap = formData.get('year');
                var formEl1 = document.forms.genderFormAtp;
                var formData1 = new FormData(formEl1);
                var genderMap = formData1.get('gender');
                formAtp(selectedElementClass.split(" ")[0]);
                formYears(selectedElementClass.split(" ")[0]);
                d3.select(".countryDiv").remove();
                drawMap(genderMap, periodMap, 1);
            } else if (selectedElementClass.split(" ")[0] === "statisticsChartButtonHeader") {
                statisticsFunction("");
            } else if(selectedElementClass.split(" ")[0] === "barChartButtonHeader"){
                removeSvg();
                d3.select(".tooltip").remove();
                var formEl = document.forms.years;
                var formData = new FormData(formEl);
                var periodBar = formData.get('year');
                var formEl1 = document.forms.genderFormAtp;
                var formData1 = new FormData(formEl1);
                var genderBar = formData1.get('gender');
                formAtp(selectedElementClass.split(" ")[0]);
                formYears(selectedElementClass.split(" ")[0]);
                drawTitlesFinalsRecords(genderBar, 1, periodBar);
                drawConnectedScatter(genderBar, periodBar, "");
            }
        });

        d3.select("div."+typeChart+"Header span")
            .style("font-weight", "bold")
            .style("color", "white");

        d3.select("div." + typeChart + "Header .buttonLineHeader div")
            .style("height", "3px");
        drawArrow();
        if (typeChart === "mapButton") {
          d3.select(".main-nav")
            .style("opacity", 1);
          formAtp(typeChart);
          formYears(typeChart);
          d3.select(".map").remove();
          drawMap("atp", "all", 0);
        } else if (typeChart === "statisticsChartButton") {
            formAtp(typeChart);
            formYears(typeChart);
            d3.select(".mainWrapper").append("div").attr("class", "statisticsDiv").attr("height", 1200).attr("width", 1400);
            searchBar();
            d3.selectAll(".hatch").style("visibility", "visible");
            drawScatterPlot("atp", "all", "");
            updateRadarChart([]);
        } else {
            formAtp(typeChart);
            formYears(typeChart);
            drawTitlesFinalsRecords("atp", 0, "all");
            drawConnectedScatter("atp", "all", "");
        }
}

function statisticsFunction(player){
  var formEl = document.forms.years;
  var formData = new FormData(formEl);
  var periodRadar = formData.get('year');
  var formEl1 = document.forms.genderFormAtp;
  var formData1 = new FormData(formEl1);
  var genderRadar = formData1.get('gender');
  if(genderRadar == "atp" && periodRadar == "1980"){
    removeSvg();
    d3.select(".tooltip").remove();
    formAtp("statisticsChartButtonHeader");
    formYears("statisticsChartButtonHeader");
    d3.select(".mainWrapper").append("div").attr("class", "warningDiv").attr("height", 600).attr("width", 400);
    let svgWarning = d3.select(".warningDiv").append("div").attr("class", "warningText").attr("position", "absolute")
                  .attr("width", 600)
                  .attr("height", 300);
    svgWarning.append("text")
        .attr("class", "warning")
        .text("Database does not contain enough information relatively to this period to show this section.");
  }
  else if(genderRadar == "wta" && periodRadar == "1980"){
    removeSvg();
    d3.select(".tooltip").remove();
    formAtp("statisticsChartButtonHeader");
    formYears("statisticsChartButtonHeader");
    d3.select(".mainWrapper").append("div").attr("class", "warningDiv").attr("height", 600).attr("width", 400);
    let svgWarning = d3.select(".warningDiv").append("div").attr("class", "warningText").attr("position", "absolute")
                  .attr("width", 600)
                  .attr("height", 300);
    svgWarning.append("text")
        .attr("class", "warning")
        .text("Database does not contain enough information relatively to this period to show this section.");
  }
  else if(genderRadar == "wta" && periodRadar == "1990"){
    removeSvg();
    d3.select(".tooltip").remove();
    formAtp("statisticsChartButtonHeader");
    formYears("statisticsChartButtonHeader");
    d3.select(".mainWrapper").append("div").attr("class", "warningDiv").attr("height", 600).attr("width", 400);
    let svgWarning = d3.select(".warningDiv").append("div").attr("class", "warningText").attr("position", "absolute")
                  .attr("width", 600)
                  .attr("height", 300);
    svgWarning.append("text")
        .attr("class", "warning")
        .text("Database does not contain enough information relatively to this period to show this section.");
  }
  else if(genderRadar == "wta" && periodRadar == "2000"){
    removeSvg();
    d3.select(".tooltip").remove();
    formAtp("statisticsChartButtonHeader");
    formYears("statisticsChartButtonHeader");
    d3.select(".mainWrapper").append("div").attr("class", "warningDiv").attr("height", 600).attr("width", 400);
    let svgWarning = d3.select(".warningDiv").append("div").attr("class", "warningText").attr("position", "absolute")
                  .attr("width", 600)
                  .attr("height", 300);
    svgWarning.append("text")
        .attr("class", "warning")
        .text("Database does not contain enough information relatively to this period to show this section.");
  }
  else{
    removeSvg();
    d3.select(".tooltip").remove();
    formAtp("statisticsChartButtonHeader");
    formYears("statisticsChartButtonHeader");
    d3.select(".mainWrapper").append("div").attr("class", "statisticsDiv").attr("height", 1200).attr("width", 1400);
    searchBar();
    d3.selectAll(".hatch").style("visibility", "visible");
    drawScatterPlot(genderRadar, periodRadar, player);
    updateRadarChart([]);
  }
}

function removeSvg() {
    d3.select(".map").remove();
    d3.select(".lineCircleChartDiv").remove();
    //d3.select(".scatterPlotDiv").remove();
    d3.select(".statisticsDiv").remove();
    d3.select(".warningDiv").remove();
    d3.select(".playersDiv").remove();
    d3.select(".listDiv").remove();
    removeScatter();
    d3.select("#searchBar").remove();
    d3.selectAll(".scatterText").remove();
    removeConnectedScatter();
}

let players = [];

function searchBar(){
  players = [];
  let mainWrapper = d3.select(".statisticsDiv");
  let form = mainWrapper.append("form").attr("id", "searchBar").attr("autocomplete", "off");
  let barWrapper = form.append("div").attr("class", "searchBarInput").attr("style", "width:250px").style("float", "right");
  barWrapper.append("input").attr("id", "searchInput").attr("type", "text").attr("placeholder", "Search player...");

  var formEl = document.forms.years;
  var formData = new FormData(formEl);
  var periodRadar = formData.get('year');
  var formEl1 = document.forms.genderFormAtp;
  var formData1 = new FormData(formEl1);
  var genderRadar = formData1.get('gender');

  d3.queue()
    .defer(d3.csv, "data/preprocessed/radar/"+ genderRadar +"_dataFullPCA_"+ periodRadar +".csv")
    .await(prepareList);

  function prepareList(error, data){
    data.forEach(function(row) {
      if(!players.includes(row.name))
        players.push(row.name);
    });
  }

  autocomplete(document.getElementById("searchInput"), players);
}

function autocomplete(inp, arr) {
  var currentFocus;
  var player;
  inp.addEventListener("input", function(e) {
      var a, b, i, val = this.value;
      closeAllLists();
      if (!val) { return false;}
      currentFocus = -1;
      a = document.createElement("DIV");
      a.setAttribute("id", this.id + "autocomplete-list");
      a.setAttribute("class", "autocomplete-items");
      this.parentNode.appendChild(a);
      for (i = 0; i < arr.length; i++) {
        if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
          b = document.createElement("DIV");
          b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
          b.innerHTML += arr[i].substr(val.length);
          b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
              b.addEventListener("click", function(e) {
              inp.value = this.getElementsByTagName("input")[0].value;
              player = inp.value;
              closeAllLists();
              updateScatterPlotSearch(player);
              searchFor(player);
          });
          a.appendChild(b);
        }
      }
  });

  inp.addEventListener("keydown", function(e) {
      var x = document.getElementById(this.id + "autocomplete-list");
      if (x) x = x.getElementsByTagName("div");
      if (e.keyCode == 40) {  //down
        currentFocus++;
        addActive(x);
        if(currentFocus > 16){
          x.scrollTop = 50;
        }
      } else if (e.keyCode == 38) { //up
        currentFocus--;
        addActive(x);
      } else if (e.keyCode == 13) {  //enter
        e.preventDefault();
        if (currentFocus > -1) {
          if (x){
            x[currentFocus].click();
          }
        }
      }
  });

  function addActive(x) {
    if (!x) return false;
    removeActive(x);
    if (currentFocus >= x.length) currentFocus = 0;
    if (currentFocus < 0) currentFocus = (x.length - 1);
    x[currentFocus].classList.add("autocomplete-active");
	  if(x[currentFocus].offsetTop < x[currentFocus].parentNode.scrollTop) {
		// Hidden on top, move scroll to show item
		// Just to the top of item
		  x[currentFocus].parentNode.scrollTop = x[currentFocus].offsetTop;
	   } else if(x[currentFocus].offsetTop > (x[currentFocus].parentNode.scrollTop + x[currentFocus].parentNode.clientHeight) - x[currentFocus].clientHeight) {
		// Hidden on bottom, move scroll to top of item + item height
		  x[currentFocus].parentNode.scrollTop = x[currentFocus].offsetTop - (x[currentFocus].parentNode.clientHeight - x[currentFocus].clientHeight);
    }
  }

  function removeActive(x) {
    for (var i = 0; i < x.length; i++) {
      x[i].classList.remove("autocomplete-active");
    }
  }

  function closeAllLists(elmnt) {
    var x = document.getElementsByClassName("autocomplete-items");
    for (var i = 0; i < x.length; i++) {
      if (elmnt != x[i] && elmnt != inp) {
      x[i].parentNode.removeChild(x[i]);
    }
  }
}
}

var gender = "atp";
var period = "all";

function formAtp(chart) {
    d3.select("#genderFormAtp").remove();
    let mainWrapper = d3.select(".mainWrapper");
    let form = mainWrapper.append("form").attr("id", "genderFormAtp");
    let inputsWrapper = form.append("div").attr("class", "mapInputs");
    if(gender == "atp"){
      inputsWrapper.append("input").attr("id", "atp").attr("type", "radio").attr("name", "gender").attr("value", "atp").attr("checked", "true");
      inputsWrapper.append("label").attr("for", "atp").html("ATP");
      inputsWrapper.append("input").attr("id", "wta").attr("type", "radio").attr("name", "gender").attr("value", "wta");
      inputsWrapper.append("label").attr("for", "wta").html("WTA");
    }
    else{
      inputsWrapper.append("input").attr("id", "atp").attr("type", "radio").attr("name", "gender").attr("value", "atp");
      inputsWrapper.append("label").attr("for", "atp").html("ATP");
      inputsWrapper.append("input").attr("id", "wta").attr("type", "radio").attr("name", "gender").attr("value", "wta").attr("checked", "true");
      inputsWrapper.append("label").attr("for", "wta").html("WTA");
    }


    d3.selectAll("#genderFormAtp input").on("change", function(){
          var formEl = document.forms.years;
          var formData = new FormData(formEl);
          period = formData.get('year');
          var formEl1 = document.forms.genderFormAtp;
          var formData1 = new FormData(formEl1);
          gender = formData1.get('gender');
          if(chart == "statisticsChartButton" || chart == "statisticsChartButtonHeader"){
              if(gender == "atp" && period == "1980"){
                removeSvg();
                d3.select(".tooltip").remove();
                formAtp(chart);
                formYears(chart);
                d3.select(".mainWrapper").append("div").attr("class", "warningDiv").attr("height", 600).attr("width", 400);
                let svgWarning = d3.select(".warningDiv").append("div").attr("class", "warningText").attr("position", "absolute")
                              .attr("width", 600)
                              .attr("height", 300);
                svgWarning.append("text")
                    .attr("class", "warning")
                    .text("Database does not contain enough information relatively to this period to show this section.");
              }
              else if(gender == "wta" && period == "1980"){
                removeSvg();
                d3.select(".tooltip").remove();
                formAtp(chart);
                formYears(chart);
                d3.select(".mainWrapper").append("div").attr("class", "warningDiv").attr("height", 600).attr("width", 400);
                let svgWarning = d3.select(".warningDiv").append("div").attr("class", "warningText").attr("position", "absolute")
                              .attr("width", 600)
                              .attr("height", 300);
                svgWarning.append("text")
                    .attr("class", "warning")
                    .text("Database does not contain enough information relatively to this period to show this section.");
              }
              else if(gender == "wta" && period == "1990"){
                removeSvg();
                d3.select(".tooltip").remove();
                formAtp(chart);
                formYears(chart);
                d3.select(".mainWrapper").append("div").attr("class", "warningDiv").attr("height", 600).attr("width", 400);
                let svgWarning = d3.select(".warningDiv").append("div").attr("class", "warningText").attr("position", "absolute")
                              .attr("width", 600)
                              .attr("height", 300);
                svgWarning.append("text")
                    .attr("class", "warning")
                    .text("Database does not contain enough information relatively to this period to show this section.");
              }
              else if(gender == "wta" && period == "2000"){
                removeSvg();
                d3.select(".tooltip").remove();
                formAtp(chart);
                formYears(chart);
                d3.select(".mainWrapper").append("div").attr("class", "warningDiv").attr("height", 600).attr("width", 400);
                let svgWarning = d3.select(".warningDiv").append("div").attr("class", "warningText").attr("position", "absolute")
                              .attr("width", 600)
                              .attr("height", 300);
                svgWarning.append("text")
                    .attr("class", "warning")
                    .text("Database does not contain enough information relatively to this period to show this section.");
              }
              else{
                d3.select(".warningDiv").remove();
                updateScatterPlot(gender, period);
                searchFor("");
              }
          }
          else if(chart == "mapButton" || chart == "mapButtonHeader")
            updateGeneral(gender, period);
          else{
            var formEl = document.forms.years;
            var formData = new FormData(formEl);
            var periodBar = formData.get('year');
            var formEl1 = document.forms.genderFormAtp;
            var formData1 = new FormData(formEl1);
            var genderBar = formData1.get('gender');
            removeConnectedScatter();
            drawTitlesFinalsRecords(genderBar, 1, periodBar);
            //drawConnectedScatter(genderBar, periodBar, "");
            updateConnectedScatterPlot(genderBar, periodBar, "");
          }

    });

}

function formYears(chart){
  d3.select("#years").remove();
  let yearsWrapper = d3.select(".mainWrapper");
  let form1 = yearsWrapper.append("form").attr("id", "years");
  yearsWrapper = form1.append("div").attr("class", "yearInputs");
  if(period == "all"){
    yearsWrapper.append("input").attr("id", "all").attr("type", "radio").attr("name", "year").attr("value", "all").attr("checked", "true");
    yearsWrapper.append("label").attr("for", "all").html("All-time");
    yearsWrapper.append("input").attr("id", "2021").attr("type", "radio").attr("name", "year").attr("value", "2021");
    yearsWrapper.append("label").attr("for", "2021").html("2021");
    yearsWrapper.append("input").attr("id", "2020").attr("type", "radio").attr("name", "year").attr("value", "2020");
    yearsWrapper.append("label").attr("for", "2020").html("2020-2021");
    yearsWrapper.append("input").attr("id", "2010").attr("type", "radio").attr("name", "year").attr("value", "2010");
    yearsWrapper.append("label").attr("for", "2010").html("2010-2019");
    yearsWrapper.append("input").attr("id", "2000").attr("type", "radio").attr("name", "year").attr("value", "2000");
    yearsWrapper.append("label").attr("for", "2000").html("2000-2009");
    yearsWrapper.append("input").attr("id", "1990").attr("type", "radio").attr("name", "year").attr("value", "1990");
    yearsWrapper.append("label").attr("for", "1990").html("1990-1999");
    yearsWrapper.append("input").attr("id", "1980").attr("type", "radio").attr("name", "year").attr("value", "1980");
    yearsWrapper.append("label").attr("for", "1980").html("1980-1989");
  }
  else if(period == "2021"){
    yearsWrapper.append("input").attr("id", "all").attr("type", "radio").attr("name", "year").attr("value", "all");
    yearsWrapper.append("label").attr("for", "all").html("All-time");
    yearsWrapper.append("input").attr("id", "2021").attr("type", "radio").attr("name", "year").attr("value", "2021").attr("checked", "true");
    yearsWrapper.append("label").attr("for", "2021").html("2021");
    yearsWrapper.append("input").attr("id", "2020").attr("type", "radio").attr("name", "year").attr("value", "2020");
    yearsWrapper.append("label").attr("for", "2020").html("2020-2021");
    yearsWrapper.append("input").attr("id", "2010").attr("type", "radio").attr("name", "year").attr("value", "2010");
    yearsWrapper.append("label").attr("for", "2010").html("2010-2019");
    yearsWrapper.append("input").attr("id", "2000").attr("type", "radio").attr("name", "year").attr("value", "2000");
    yearsWrapper.append("label").attr("for", "2000").html("2000-2009");
    yearsWrapper.append("input").attr("id", "1990").attr("type", "radio").attr("name", "year").attr("value", "1990");
    yearsWrapper.append("label").attr("for", "1990").html("1990-1999");
    yearsWrapper.append("input").attr("id", "1980").attr("type", "radio").attr("name", "year").attr("value", "1980");
    yearsWrapper.append("label").attr("for", "1980").html("1980-1989");
  }
  else if(period == "2020"){
    yearsWrapper.append("input").attr("id", "all").attr("type", "radio").attr("name", "year").attr("value", "all");
    yearsWrapper.append("label").attr("for", "all").html("All-time");
    yearsWrapper.append("input").attr("id", "2021").attr("type", "radio").attr("name", "year").attr("value", "2021");
    yearsWrapper.append("label").attr("for", "2021").html("2021");
    yearsWrapper.append("input").attr("id", "2020").attr("type", "radio").attr("name", "year").attr("value", "2020").attr("checked", "true");
    yearsWrapper.append("label").attr("for", "2020").html("2020-2021");
    yearsWrapper.append("input").attr("id", "2010").attr("type", "radio").attr("name", "year").attr("value", "2010");
    yearsWrapper.append("label").attr("for", "2010").html("2010-2019");
    yearsWrapper.append("input").attr("id", "2000").attr("type", "radio").attr("name", "year").attr("value", "2000");
    yearsWrapper.append("label").attr("for", "2000").html("2000-2009");
    yearsWrapper.append("input").attr("id", "1990").attr("type", "radio").attr("name", "year").attr("value", "1990");
    yearsWrapper.append("label").attr("for", "1990").html("1990-1999");
    yearsWrapper.append("input").attr("id", "1980").attr("type", "radio").attr("name", "year").attr("value", "1980");
    yearsWrapper.append("label").attr("for", "1980").html("1980-1989");
  }
  else if(period == "2010"){
    yearsWrapper.append("input").attr("id", "all").attr("type", "radio").attr("name", "year").attr("value", "all");
    yearsWrapper.append("label").attr("for", "all").html("All-time");
    yearsWrapper.append("input").attr("id", "2021").attr("type", "radio").attr("name", "year").attr("value", "2021");
    yearsWrapper.append("label").attr("for", "2021").html("2021");
    yearsWrapper.append("input").attr("id", "2020").attr("type", "radio").attr("name", "year").attr("value", "2020");
    yearsWrapper.append("label").attr("for", "2020").html("2020-2021");
    yearsWrapper.append("input").attr("id", "2010").attr("type", "radio").attr("name", "year").attr("value", "2010").attr("checked", "true");
    yearsWrapper.append("label").attr("for", "2010").html("2010-2019");
    yearsWrapper.append("input").attr("id", "2000").attr("type", "radio").attr("name", "year").attr("value", "2000");
    yearsWrapper.append("label").attr("for", "2000").html("2000-2009");
    yearsWrapper.append("input").attr("id", "1990").attr("type", "radio").attr("name", "year").attr("value", "1990");
    yearsWrapper.append("label").attr("for", "1990").html("1990-1999");
    yearsWrapper.append("input").attr("id", "1980").attr("type", "radio").attr("name", "year").attr("value", "1980");
    yearsWrapper.append("label").attr("for", "1980").html("1980-1989");
  }
  else if(period == "2000"){
    yearsWrapper.append("input").attr("id", "all").attr("type", "radio").attr("name", "year").attr("value", "all");
    yearsWrapper.append("label").attr("for", "all").html("All-time");
    yearsWrapper.append("input").attr("id", "2021").attr("type", "radio").attr("name", "year").attr("value", "2021");
    yearsWrapper.append("label").attr("for", "2021").html("2021");
    yearsWrapper.append("input").attr("id", "2020").attr("type", "radio").attr("name", "year").attr("value", "2020");
    yearsWrapper.append("label").attr("for", "2020").html("2020-2021");
    yearsWrapper.append("input").attr("id", "2010").attr("type", "radio").attr("name", "year").attr("value", "2010");
    yearsWrapper.append("label").attr("for", "2010").html("2010-2019");
    yearsWrapper.append("input").attr("id", "2000").attr("type", "radio").attr("name", "year").attr("value", "2000").attr("checked", "true");
    yearsWrapper.append("label").attr("for", "2000").html("2000-2009");
    yearsWrapper.append("input").attr("id", "1990").attr("type", "radio").attr("name", "year").attr("value", "1990");
    yearsWrapper.append("label").attr("for", "1990").html("1990-1999");
    yearsWrapper.append("input").attr("id", "1980").attr("type", "radio").attr("name", "year").attr("value", "1980");
    yearsWrapper.append("label").attr("for", "1980").html("1980-1989");
  }
  else if(period == "1990"){
    yearsWrapper.append("input").attr("id", "all").attr("type", "radio").attr("name", "year").attr("value", "all");
    yearsWrapper.append("label").attr("for", "all").html("All-time");
    yearsWrapper.append("input").attr("id", "2021").attr("type", "radio").attr("name", "year").attr("value", "2021");
    yearsWrapper.append("label").attr("for", "2021").html("2021");
    yearsWrapper.append("input").attr("id", "2020").attr("type", "radio").attr("name", "year").attr("value", "2020");
    yearsWrapper.append("label").attr("for", "2020").html("2020-2021");
    yearsWrapper.append("input").attr("id", "2010").attr("type", "radio").attr("name", "year").attr("value", "2010");
    yearsWrapper.append("label").attr("for", "2010").html("2010-2019");
    yearsWrapper.append("input").attr("id", "2000").attr("type", "radio").attr("name", "year").attr("value", "2000");
    yearsWrapper.append("label").attr("for", "2000").html("2000-2009");
    yearsWrapper.append("input").attr("id", "1990").attr("type", "radio").attr("name", "year").attr("value", "1990").attr("checked", "true");
    yearsWrapper.append("label").attr("for", "1990").html("1990-1999");
    yearsWrapper.append("input").attr("id", "1980").attr("type", "radio").attr("name", "year").attr("value", "1980");
    yearsWrapper.append("label").attr("for", "1980").html("1980-1989");
  }
  else if(period == "1980"){
    yearsWrapper.append("input").attr("id", "all").attr("type", "radio").attr("name", "year").attr("value", "all");
    yearsWrapper.append("label").attr("for", "all").html("All-time");
    yearsWrapper.append("input").attr("id", "2021").attr("type", "radio").attr("name", "year").attr("value", "2021");
    yearsWrapper.append("label").attr("for", "2021").html("2021");
    yearsWrapper.append("input").attr("id", "2020").attr("type", "radio").attr("name", "year").attr("value", "2020");
    yearsWrapper.append("label").attr("for", "2020").html("2020-2021");
    yearsWrapper.append("input").attr("id", "2010").attr("type", "radio").attr("name", "year").attr("value", "2010");
    yearsWrapper.append("label").attr("for", "2010").html("2010-2019");
    yearsWrapper.append("input").attr("id", "2000").attr("type", "radio").attr("name", "year").attr("value", "2000");
    yearsWrapper.append("label").attr("for", "2000").html("2000-2009");
    yearsWrapper.append("input").attr("id", "1990").attr("type", "radio").attr("name", "year").attr("value", "1990");
    yearsWrapper.append("label").attr("for", "1990").html("1990-1999");
    yearsWrapper.append("input").attr("id", "1980").attr("type", "radio").attr("name", "year").attr("value", "1980").attr("checked", "true");
    yearsWrapper.append("label").attr("for", "1980").html("1980-1989");
  }


  d3.selectAll("#years input").on("change", function(){
    var formEl = document.forms.years;
    var formData = new FormData(formEl);
    period = formData.get('year');
    var formEl1 = document.forms.genderFormAtp;
    var formData1 = new FormData(formEl1);
    gender = formData1.get('gender');
    if(chart == "statisticsChartButton" || chart == "statisticsChartButtonHeader"){
      if(gender == "atp" && period == "1980"){
        removeSvg();
        d3.select(".tooltip").remove();
        formAtp(chart);
        formYears(chart);
        d3.select(".mainWrapper").append("div").attr("class", "warningDiv").attr("height", 600).attr("width", 400);
        let svgWarning = d3.select(".warningDiv").append("div").attr("class", "warningText").attr("position", "absolute")
                      .attr("width", 600)
                      .attr("height", 300);
        svgWarning.append("text")
            .attr("class", "warning")
            .text("Database does not contain enough information relatively to this period to show this section.");
      }
      else if(gender == "wta" && period == "1980"){
        removeSvg();
        d3.select(".tooltip").remove();
        formAtp(chart);
        formYears(chart);
        d3.select(".mainWrapper").append("div").attr("class", "warningDiv").attr("height", 600).attr("width", 400);
        let svgWarning = d3.select(".warningDiv").append("div").attr("class", "warningText").attr("position", "absolute")
                      .attr("width", 600)
                      .attr("height", 300);
        svgWarning.append("text")
            .attr("class", "warning")
            .text("Database does not contain enough information relatively to this period to show this section.");
      }
      else if(gender == "wta" && period == "1990"){
        removeSvg();
        d3.select(".tooltip").remove();
        formAtp(chart);
        formYears(chart);
        d3.select(".mainWrapper").append("div").attr("class", "warningDiv").attr("height", 600).attr("width", 400);
        let svgWarning = d3.select(".warningDiv").append("div").attr("class", "warningText").attr("position", "absolute")
                      .attr("width", 600)
                      .attr("height", 300);
        svgWarning.append("text")
            .attr("class", "warning")
            .text("Database does not contain enough information relatively to this period to show this section.");
      }
      else if(gender == "wta" && period == "2000"){
        removeSvg();
        d3.select(".tooltip").remove();
        formAtp(chart);
        formYears(chart);
        d3.select(".mainWrapper").append("div").attr("class", "warningDiv").attr("height", 600).attr("width", 400);
        let svgWarning = d3.select(".warningDiv").append("div").attr("class", "warningText").attr("position", "absolute")
                      .attr("width", 600)
                      .attr("height", 300);
        svgWarning.append("text")
            .attr("class", "warning")
            .text("Database does not contain enough information relatively to this period to show this section.");
      }
      else{
        d3.select(".warningDiv").remove();
        var formEl = document.forms.years;
        var formData = new FormData(formEl);
        var periodScatter = formData.get('year');
        var formEl1 = document.forms.genderFormAtp;
        var formData1 = new FormData(formEl1);
        var genderScatter = formData1.get('gender');
        updateScatterPlot(genderScatter, periodScatter);
        searchFor("");
      }
    }
    else if(chart == "mapButton" || chart == "mapButtonHeader")
      updateGeneral(gender, period);
    else{
      var formEl = document.forms.years;
      var formData = new FormData(formEl);
      var periodBar = formData.get('year');
      var formEl1 = document.forms.genderFormAtp;
      var formData1 = new FormData(formEl1);
      var genderBar = formData1.get('gender');
      removeConnectedScatter();
      drawTitlesFinalsRecords(genderBar, 1, periodBar);
      //drawConnectedScatter(genderBar, periodBar, "");
      updateConnectedScatterPlot(genderBar, periodBar, "");
    }
  });
}


//Draw the arrow to go back to the main page
function drawArrow(){
   let arrow = d3.select("body").append("div").attr("class","arrow");
   arrow.append("a").attr("class", "to-top").attr("href", "#");

   d3.select(".arrow")
       .on("click", function() {
           d3.select(".tooltip").remove();
           d3.select(".arrow").attr("opacity", 0).transition().duration(500).attr("opacity", 1).remove()
           d3.select(".mainWrapper")
               .attr("opacity", 1)
               .transition()
               .duration(900)
               .style("top", "200%")
               .attr("opacity", 0)
               .remove()
               .on("end", function() {
                   let mainWrapper = d3.select("body").append("div").attr("class", "mainWrapper");
                   drawTitlePageLayout(mainWrapper);
                   drawInitialButtons();
               });
             d3.select(".main-nav")
               .style("opacity", 0);
       })
}

document.addEventListener('DOMContentLoaded', function(){
    let mainWrapper = d3.select("body").append("div").attr("class", "mainWrapper");
    drawTitlePageLayout(mainWrapper);
    drawInitialButtons();
    d3.select("div.main-nav").style("opacity", 0);
})
