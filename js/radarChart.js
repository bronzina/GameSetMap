function drawRadarChart(data, names){

    d3.select("#radarChartDiv").remove();

    d3.select(".statisticsDiv").append("div").attr("id", "radarChartDiv")
      .attr("width", 450)
      .attr("height", 450)
      .style("max-width", 500);

  var w = 350,
	h = 350;

  //var colorscale = d3.scaleOrdinal(d3.schemeCategory10);
  var colorscale = d3.scaleOrdinal(["#3300FF", "#FF6600", "#FFCC00", "#FF66CC", "#00CCFF"]);

  //Legend titles
  var LegendOptions = [];
  for(i=0; i < names.length; i++){
    LegendOptions.push(names[i]);
  }

    //Options for the Radar chart, other than default
    var mycfg = {
      w: w,
      h: h,
      maxValue: 0.6,
      levels: 6,
      ExtraWidthX: 200
    }

    //Call function to draw the radar chart
    drawRadar("#radarChartDiv", data, mycfg);

    //Initiate legend
     d3.select("#radarLegend").remove();

     var svg = d3.select('.statisticsDiv')
     .select("#radarChartDiv")
 	   .append('svg')
      .attr("id", "radarLegend")
 	   .attr("width", 300)
 	   .attr("height", 150)
      .attr("transform", "translate(-130, -70)")
      .style("position", "relative")
      .style("float", "bottom");

     //Create the title for the legend
    var text = svg.append("text")
	   .attr("class", "title")
	   .attr('transform', 'translate(-230, 15)')
	   .attr("x", 250)
	   .attr("y", 10)
	   .attr("font-size", "15px")
	   .attr("fill", "#ffffff")
	   .text("Statistics in % of the following players:");

     //Initiate Legend
    var legend = svg.append("g")
	    .attr("class", "legend")
	    .attr("height", 100)
	    .attr("width", 200);

	   //Create colour squares
	 legend.selectAll('rect')
	  .data(LegendOptions)
	  .enter()
	  .append("rect")
	  .attr("x", 30)
	  .attr("y", function(d, i){ return i * 20+35;})
	  .attr("width", 15)
	  .attr("height", 15)
	  .style("fill", function(d, i){ return colorscale(i);});

var activated = false;

	//Create text next to squares
	legend.selectAll('text')
	  .data(LegendOptions)
	  .enter()
	  .append("text")
	  .attr("x", 50)
	  .attr("y", function(d, i){ return i * 20 + 48;})
	  .attr("font-size", "15px")
	  .attr("fill", "#ffffff")
	  .text(function(d) { return d; })
    .on("mouseover", function(){
      d3.select(this).style("cursor", "pointer");
    })
    .on("mouseout", function(){
      d3.select(this).style("cursor", "default");
    })
    .on("click", function(d, i){
      if(!activated){
        activated = true;
        d3.selectAll("polygon")
           .transition(200)
           .style("fill-opacity", 0.0);
        d3.select("#polygon" + i.toString()).raise();
        d3.select("#polygon" + i.toString())
           .transition(200)
           .style("fill-opacity", 0.9);
      }
      else{
        activated = false;
        d3.selectAll("polygon")
           .transition(200)
           .style("fill-opacity", 0.0);
      }
    });


    function drawRadar(id, d, options){
        var cfg = {
	         radius: 5,
	         w: 200,
	         h: 200,
	         factor: 1,
	         factorLegend: .85,
	         levels: 3,
	         maxValue: 0,
	         radians: 2 * Math.PI,
	         opacityArea: 0.1,
	         ToRight: 5,
	         TranslateX: 80,
	         TranslateY: 25,
	         ExtraWidthX: 100,
	         ExtraWidthY: 60,
	         //color: d3.scaleOrdinal(d3.schemeCategory10)
           color: d3.scaleOrdinal(["#3300FF", "#FF6600", "#FFCC00", "#FF66CC", "#00CCFF"])
	      };


	       if('undefined' !== typeof options){
	          for(var i in options){
		            if('undefined' !== typeof options[i]){
		                cfg[i] = options[i];
		             }
	          }
	       };

         if(d != []){
           cfg.maxValue = 1;
  	       var allAxis = (d[0].map(function(i, j){return i.axis}));
  	       var total = allAxis.length;
  	       var radius = cfg.factor * Math.min(cfg.w/2, cfg.h/2);
  	       var Format = d3.format('.0%');
  	       d3.select(id).select("svg").remove();
        }
        else{
          d.push(["", {axis:"Ace", value:0}, {axis:"Double faults", value:0},
                  {axis:"1st Won", value:0}, {axis:"2nd Won", value: 0},
                  {axis:"Break Points Saved", value:0}, {axis:"Break Points Lost", value:0}]);
        }

	       var g = d3.select(id)
			      .append("svg")
            .attr("id", "radarChart")
			      .attr("width", cfg.w+cfg.ExtraWidthX)
			      .attr("height", cfg.h+cfg.ExtraWidthY)
			      .append("g")
			      .attr("transform", "translate(" + cfg.TranslateX + "," + cfg.TranslateY + ")");

	     var tooltip;

	      //Circular segments
	     for(var j=0; j<cfg.levels; j++){
	        var levelFactor = cfg.factor*radius*((j+1)/cfg.levels);
	        g.selectAll(".levels")
	         .data(allAxis)
	         .enter()
	         .append("svg:line")
	         .attr("x1", function(d, i){return levelFactor * (1-cfg.factor*Math.sin(i*cfg.radians/total));})
	         .attr("y1", function(d, i){return levelFactor * (1-cfg.factor*Math.cos(i*cfg.radians/total));})
	         .attr("x2", function(d, i){return levelFactor * (1-cfg.factor*Math.sin((i+1)*cfg.radians/total));})
	         .attr("y2", function(d, i){return levelFactor * (1-cfg.factor*Math.cos((i+1)*cfg.radians/total));})
	         .attr("class", "line")
	         .style("stroke", "grey")
	         .style("stroke-opacity", "0.75")
	         .style("stroke-width", "0.3px")
	         .attr("transform", "translate(" + (cfg.w/2-levelFactor) + ", " + (cfg.h/2-levelFactor) + ")");
	      }

	       //Text indicating at what % each level is
	      for(var j=0; j<cfg.levels; j++){
	         var levelFactor = cfg.factor*radius*((j+1)/cfg.levels);
	         g.selectAll(".levels")
	          .data([1]) //dummy data
	          .enter()
	          .append("svg:text")
	          .attr("x", function(d){return levelFactor*(1-cfg.factor*Math.sin(0));})
	          .attr("y", function(d){return levelFactor*(1-cfg.factor*Math.cos(0));})
	          .attr("class", "legend")
	          .style("font-family", "sans-serif")
	          .style("font-size", "10px")
	          .attr("transform", "translate(" + (cfg.w/2-levelFactor + cfg.ToRight) + ", " + (cfg.h/2-levelFactor) + ")")
	          .attr("fill", "#737373")
	          .text(Format((j+1)*cfg.maxValue/cfg.levels));
	      }

	      series = 0;

	      var axis = g.selectAll(".axis")
			     .data(allAxis)
			     .enter()
			     .append("g")
			     .attr("class", "axis");

	      axis.append("line")
		     .attr("x1", cfg.w/2)
		     .attr("y1", cfg.h/2)
		     .attr("x2", function(d, i){return cfg.w/2*(1-cfg.factor*Math.sin(i*cfg.radians/total));})
		     .attr("y2", function(d, i){return cfg.h/2*(1-cfg.factor*Math.cos(i*cfg.radians/total));})
		     .attr("class", "line")
		     .style("stroke", "grey")
		     .style("stroke-width", "1px");

	      axis.append("text")
		     .attr("class", "legend")
		     .text(function(d){return d})
		     .style("font-family", "sans-serif")
		     .style("font-size", "11px")
         .style("fill", "#ffffff")
		     .attr("text-anchor", "middle")
		     .attr("dy", "1.5em")
		     .attr("transform", function(d, i){return "translate(0, -10)"})
		     .attr("x", function(d, i){return cfg.w/2*(1-cfg.factorLegend*Math.sin(i*cfg.radians/total))-60*Math.sin(i*cfg.radians/total);})
		     .attr("y", function(d, i){return cfg.h/2*(1-Math.cos(i*cfg.radians/total))-20*Math.cos(i*cfg.radians/total);});

         var i=0;
	      d.forEach(function(y, x){
	         dataValues = [];
	         g.selectAll(".nodes")
		         .data(y, function(j, i){
		             dataValues.push([
			                cfg.w/2*(1-(parseFloat(Math.max(j.value, 0))/cfg.maxValue)*cfg.factor*Math.sin(i*cfg.radians/total)),
			                cfg.h/2*(1-(parseFloat(Math.max(j.value, 0))/cfg.maxValue)*cfg.factor*Math.cos(i*cfg.radians/total))
		             ]);
		         });
	         dataValues.push(dataValues[0]);
	         g.selectAll(".area")
					  .data([dataValues])
					  .enter()
					  .append("polygon")
					  .attr("class", "radar-chart-serie"+series)
            .attr("id", "polygon" + i.toString())
					  .style("stroke-width", "2px")
					  .style("stroke", cfg.color(series))
					  .attr("points",function(d) {
						  var str="";
						  for(var pti=0;pti<d.length;pti++){
							  str=str+d[pti][0]+","+d[pti][1]+" ";
						  }
						  return str;
					   })
					 .style("fill", function(j, i){return cfg.color(series)})
					 .style("fill-opacity", cfg.opacityArea)
					 .on('mouseover', function (d, i){
							z = "polygon."+d3.select(this).attr("class");
							g.selectAll("polygon")
								 .transition(200)
                 .style("z-index", 0)
								 .style("fill-opacity", 0.0);
							g.selectAll(z)
								 .transition(200)
                 .style("z-index", 99)
								 .style("fill-opacity", 0.9);
              d3.select(this).raise();
						})
					 .on('mouseout', function(){
							g.selectAll("polygon")
							   .transition(200)
								 .style("fill-opacity", cfg.opacityArea);
              d3.select(this).lower();
					 });
	       series++;
         i++;
	    });
	    series=0;


	    d.forEach(function(y, x){
	       g.selectAll(".nodes")
		       .data(y).enter()
		       .append("svg:circle")
		       .attr("class", "radar-chart-serie"+series)
		       .attr('r', cfg.radius)
		       .attr("alt", function(j){return Math.max(j.value, 0)})
		       .attr("cx", function(j, i){
		           dataValues.push([
			              cfg.w/2*(1-(parseFloat(Math.max(j.value, 0))/cfg.maxValue)*cfg.factor*Math.sin(i*cfg.radians/total)),
			              cfg.h/2*(1-(parseFloat(Math.max(j.value, 0))/cfg.maxValue)*cfg.factor*Math.cos(i*cfg.radians/total))
		            ]);
		           return cfg.w/2*(1-(Math.max(j.value, 0)/cfg.maxValue)*cfg.factor*Math.sin(i*cfg.radians/total));
		       })
		       .attr("cy", function(j, i){
		           return cfg.h/2*(1-(Math.max(j.value, 0)/cfg.maxValue)*cfg.factor*Math.cos(i*cfg.radians/total));
		        })
		       .attr("data-id", function(j){return j.axis})
		       .style("fill", cfg.color(series)).style("fill-opacity", .9)
           .style("fill-opacity", .9)
		       .on('mouseover', function (d){
					    newX =  parseFloat(d3.select(this).attr('cx')) - 10;
					    newY =  parseFloat(d3.select(this).attr('cy')) - 5;

					    tooltip
						    .attr('x', newX)
						    .attr('y', newY)
						    .text(Format(d.value))
						    .transition(200)
						    .style('opacity', 1);

					    z = "polygon." + d3.select(this).attr("class");
					    g.selectAll("polygon")
						    .transition(200)
						    .style("fill-opacity", 0.0);
					    g.selectAll(z)
						    .transition(200)
						    .style("fill-opacity", 0.9);
				    })
		       .on('mouseout', function(){
					    tooltip
						    .transition(200)
						    .style('opacity', 0);
					    g.selectAll("polygon")
						    .transition(200)
						    .style("fill-opacity", cfg.opacityArea);
				    })
		       .append("svg:title")
		       .text(function(j){return Math.max(j.value, 0)});
	       series++;
	     });

    	//Tooltip
    	tooltip = g.append('text')
			   .style('opacity', 0)
         .style("fill", "#ffffff")
			   .style('font-family', 'sans-serif')
			   .style('font-size', '13px');
   }
}

function updateRadarChart(players){
  var names = [];
  var data = [[
  {axis:"Ace",value:0},
  {axis:"Double faults",value:0},
  {axis:"1st Serve Won",value:0},
  {axis:"2nd Serve Won",value:0},
  {axis:"Break Points Saved",value:0},
  {axis:"Break Points Won",value:0},
  ]];

  for(i=0; i < players.length-1; i++){
      data.push([
      {axis:"Ace",value:0},
      {axis:"Double faults",value:0},
      {axis:"1st Serve Won",value:0},
      {axis:"2nd Serve Won",value:0},
      {axis:"Break Points Saved",value:0},
      {axis:"Break Points Won",value:0},
    ]);
  }

  if(players != []){
    for(i=0; i < players.length; i++){
      data[i] = ([{axis:"Ace", value:players[i].ace}, {axis:"Double faults", value:players[i].df},
              {axis:"1st Serve Won", value:players[i]["1stWon"]}, {axis:"2nd Serve Won", value: players[i]["2ndWon"]},
              {axis:"Break Points Saved", value:players[i].bpSaved}, {axis:"Break Points Won", value:players[i].bpLost}]);
      names[i] = players[i].name;
    }
  }

  drawRadarChart(data, names);
}
