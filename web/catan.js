function shuffleArray(array) {
  for(var i = array.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var temp = array[i];
      array[i] = array[j];
      array[j] = temp;
  }
  return array;
}

function cornerNext(t) {
  var index = parseInt($(t).attr("id").substring(6, $(t).attr("id").length));
  var state = game["corners"][index]%10;
  if(state == undefined || isNaN(state)) state = 0;
  state++;
  if(state === 3) state = 0;
  game["corners"][index] = state+10*team;

  $(t).removeClass("state0").removeClass("state1").removeClass("state2");
  $(t).addClass("state"+state);

  $(t).css("background-color", teamcolors[team]);
  if(state === 0) $(t).css("background-color", "black");

};

var game = {};
var ateam = {"wood":0, "wheat":0, "sheep":0, "brick":0, "ore":0, "dev":[]};
game["teams"] = {0: $.extend(true, {}, ateam), 1:$.extend(true, {}, ateam), 2:$.extend(true, {}, ateam), 3:$.extend(true, {}, ateam)};
//dev cards: 0 - soldier, 1 - VP, 2 - monopoly, 3 -Road build, 4 - year of plenty
game["devs"] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,2,2,3,3,4,4];
game["devs"] = shuffleArray(game["devs"]);
game["wood"] = 19;
game["brick"] = 19;
game["wheat"] = 19;
game["sheep"] = 19;
game["ore"] = 19;


var team = 0;
var teamcolors = ["red", "blue", "orange", "purple"];
//0 - desert, 1 - wood, 2 - brick, 3 - sheep, 4 - wheat, 5 - ore
var colors = ["#cc9900", "green", "#cc3300", "#66ff33", "#ffff00", "gray"];
game["tiles"] = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5];
game["numbers"] = [2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12];
game["numbers"] = shuffleArray(game["numbers"]);
game["tiles"] = shuffleArray(game["tiles"]);

//add desert
var rand = Math.floor(Math.random() * game["tiles"].length);
game["tiles"].splice(rand, 0, 0);
game["numbers"].splice(rand, 0, 0);


var degs = [340,45,340,90,270,90,200,200,160];
game["ports"] = [1,2,3,4,5,0,0,0,0];
game["ports"] = shuffleArray(game["ports"]);

var corner = 0;
game["corners"] = [];

function draw() {

$(".corner").remove();

$(".hex:not(.invis, .port)").each(function(i) {
  $(this).find(".top").css("border-bottom","30px solid " + colors[game["tiles"][i]]);
  $(this).find(".middle").css("background", colors[game["tiles"][i]]);
  $(this).find(".bottom").css("border-top","30px solid " + colors[game["tiles"][i]]);
  $(this).find(".middle").text(game["numbers"][i]);
  $(this).find(".top").append("<div class=\"corner tlcorner\" id=\"corner"+corner+"\"></div><div class=\"corner ttcorner\" id=\"corner"+(corner+1)+"\"></div><div class=\"corner trcorner\" id=\"corner"+(corner+2)+"\"></div>");
  $(this).find(".bottom").append("<div class=\"corner blcorner\" id=\"corner"+(corner+3)+"\"></div><div class=\"corner bbcorner\" id=\"corner"+(corner+4)+"\"></div><div class=\"corner brcorner\" id=\"corner"+(corner+5)+"\"></div>");
  corner += 6;
});

$(".port").each(function(i) {
  $(this).find(".top").css("border-bottom","30px solid transparent");
  $(this).find(".middle").css("background", "transparent");
  $(this).find(".bottom").css("border-top","30px solid " + colors[game["ports"][i]]);
  $(this).css("transform","rotate(" + degs[i]+ "deg)");
});

$(".corner").each(function(i) {
  if(game["corners"][i] > 0) {
    var num = game["corners"][i];
    game["corners"][i] = 0;
    for(var j=0;j<num;j++) {
      cornerNext(this);
    }
  }

});

$(".corner").click(function() {
  cornerNext(this);
});

$("#wheat").text("Wheat: " + game["teams"][team]["wheat"]); 
$("#wood").text("Wood: " + game["teams"][team]["wood"]); 
$("#brick").text("Brick: " + game["teams"][team]["brick"]); 
$("#sheep").text("Sheep: " + game["teams"][team]["sheep"]); 
$("#ore").text("Ore: " + game["teams"][team]["ore"]); 

console.log("redrawn");
}
draw();

$(".addcard").click(function() {
  var res = $(this).attr("res");
  if(game[res] > 0) {
    game[res]--;
    game["teams"][team][res]++;
  }
  draw();
});
$(".res").click(function() {
  var res = $(this).attr("id");
  if(game["teams"][team][res] > 0) {
    game[res]++;
    game["teams"][team][res]--;
  }
  draw();
});

$("#teamselect").change(function() {
  team = parseInt($(this).val());
});

$(".corner").click(function() {
  cornerNext(this);
});


