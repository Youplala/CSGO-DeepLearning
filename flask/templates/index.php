<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href='../static/main.css' />

    <title>CS:GO Predictor</title>
  </head>
  <body>

  <p id="selectedBool" hidden>{{ selected }}</p>
  <p id="team1variable" hidden>{{ team1 }}</p>
  <p id="team2variable" hidden>{{ team2 }}</p>

 <div class="main">

    <div class="left">
       <div class="center-top">
         <p>salut</p>
         <p>jtm</p>
       </div>
    </div>
    <div class="center">
      <img src="static/logo.png" alt="">
      <div class="pick">
        <div class="card" id="team1_selected">
          <p id="select_team1_text">Select team 1 below</p>
          <div class="team" id="selected1" style="display:none;">
            <img id="logo1" src="" alt="">
            <p id="team1Name">vitality</p>
          </div>
        </div>
        <div class="">
          <p style="font-size:50px;">2 - 16</p>
          <a href="">Reset</a>
        </div>
        <div class="card" id="team2_selected">
          <p id="select_team2_text">Select team 2 below</p>
          <div class="team" id="selected2" style="display:none;">
            <img id="logo2" src="" alt="">
            <p id="team2Name">vitality</p>
          </div>
        </div>

      </div>

      <form method="post" action="/" class="predict_btn">
        <input type="submit" value="Predict" name="predict"/>
        <input id="team1input" type="text" name="team1input" value="" hidden>
        <input id="team2input" type="text" name="team2input" value="" hidden>
      </form>


      <div class="teams">

        {% for key,team in data.iterrows() %}
          <div class="team" onclick="select_team(this)">
            <img src="{{ team['logos'] }}" alt="">
              <p> {{ team['team'] }} </p>
          </div>
        {% endfor %}



      </div>
    </div>
    <div class="right">
    </div>
 </div>


 <script type="text/javascript">



if(document.getElementById('selectedBool').textContent === "true"){
  select_team1_text.style.display = "none";
  select_team2_text.style.display = "none";
  var team_container1 = document.getElementById('selected1');
  var team_container2 = document.getElementById('selected2');
  team1Name = document.getElementById('team1variable').textContent;
  team2Name = document.getElementById('team2variable').textContent;
  document.getElementById('team1Name').textContent = team1Name;
  team_container1.style.display="block";
  document.getElementById("team1input").value = team1Name;
  document.getElementById('team2Name').textContent = team2Name;
  team_container2.style.display="block";
  document.getElementById("team2input").value = team2Name;
}

 function select_team(team){
     team.style.border = "2px solid #6E509F";
     var childs = team.childNodes;
     var logo = childs[1].src;
     var teamName = team.getElementsByTagName('p')[0].innerHTML;
     var team_container1 = document.getElementById('selected1');
     var team_container2 = document.getElementById('selected2');
     if (team_container1.style.display == "none"){
       var select_team1_text = document.getElementById('select_team1_text');
       select_team1_text.style.display = "none";
       document.getElementById('logo1').src = logo;
       document.getElementById('team1Name').textContent = teamName;
       team_container1.style.display="block";
       document.getElementById("team1input").value = teamName;
     }else{
       var select_team2_text = document.getElementById('select_team2_text');
       select_team2_text.style.display = "none";
       document.getElementById('logo2').src = logo;
       document.getElementById('team2Name').textContent = teamName;
       team_container2.style.display="block";
       document.getElementById("team2input").value = teamName;
     }


 }



 </script>
 </body>

</html>
