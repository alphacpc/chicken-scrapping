// set the dimensions and margins of the graph
var margin = {top: 10, right: 100, bottom: 30, left: 60},
    width = 980 - margin.left - margin.right,
    height = 600 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3.select("#divGraph")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

//Read the data
d3.json("http://localhost:5000/api/data/viz", function(data) {

    console.log(data)

    var allGroup = ["guinarshop.com", "auchan.fr", "baayguins.com"]

    // Reformat the data: we need an array of arrays of {x, y} tuples
    var dataReady = allGroup.map( (grpName) => { // .map allows to do something for each element of the list
      return {
        name: grpName,
        values: data.filter(d => {
          if(d['origine'] == grpName){
            return {poids: d.poids, value: d['prix']};
          }
        })
      };
    });

    console.log("Valeur dataReady real data :",dataReady)

    // A color scale: one color for each group
    var myColor = d3.scaleOrdinal()
    .domain(allGroup)
    .range(d3.schemeSet2);

    // axis X 
    let x = d3.scaleLinear()
        .domain([0.9, 2.3])
        .range([ 0, width ]);
    
    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));
  
    // axis Y
      var y = d3.scaleLinear()
        .domain( [0, 12000])
        .range([ height, 0 ]);
      svg.append("g")
        .call(d3.axisLeft(y));

    
    
    // Add the lines
        var line = d3.line()
        .x((d) => x(+d.poids) )
        .y((d) => y(+d.prix) )
      svg.selectAll("myLines")
        .data(dataReady)
        .enter()
        .append("path")
          .attr("class", (d) => d.name )
          .attr("d", (d) => line(d.values) )
          .attr("stroke", (d) => myColor(d.name) )
          .style("stroke-width", 4)
          .style("fill", "none")
    
      
          // Add the points
        svg
        // First we need to enter in a group
        .selectAll("myDots")
        .data(dataReady)
        .enter()
          .append('g')
          .style("fill", (d) => { 
            console.log(d.name)
            console.log(myColor(d.name))
            return myColor(d.name) 
          })
          .attr("class", (d) => d.name )
        // Second we need to enter in the 'values' part of this group
        .selectAll("myPoints")
        .data(function(d){ return d.values })
        .enter()
        .append("circle")
          .attr("cx", (d) => x(d.poids)  )
          .attr("cy", (d) => y(d.prix)  )
          .attr("r", 5)
          .attr("stroke", "white")
        





    // Add a legend (interactive)
    svg
      .selectAll("myLegend")
      .data(dataReady)
      .enter()
        .append('g')
        .append("text")
          .attr('x', function(d,i){ return 30 + i*120})
          .attr('y', 30)
          .text(function(d) { return d.name; })
          .style("fill", function(d){ return myColor(d.name) })
          .style("font-size", 15)
        
})