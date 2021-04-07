<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href='../static/main.css' />
    <link rel="preconnect" href="https://fonts.gstatic.com">

    <link href="https://fonts.googleapis.com/css2?family=Rubik&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <link rel="stylesheet" href="../static/index_bis.css">
    <link rel="stylesheet" href="../static/highchart.css">
    <title>CS:GO Predictor</title>
  </head>
  <body>


    <script src="https://code.highcharts.com/stock/highstock.js"></script>
    <script src="https://code.highcharts.com/stock/modules/data.js"></script>
    <script src="https://code.highcharts.com/stock/modules/exporting.js"></script>
    <script src="https://code.highcharts.com/stock/modules/export-data.js"></script>

       <script>


var data =
        [
          //[date,TimeStamp,Correct_TimeStamp,Rank_Astralis,Rank_Big,Rank_Complexity,Rank_EG,Rank_Fnatic,Rank_G2,Rank_Gambit,Rank_Heroic,Rank_Liquid,Rank_Mouses,Rank_NAVI,Rank_OG,Rank_Spirit,rank_Virtus_pro,Rank_Vitality],
          [12_2_2019,1575244800,1575244800000,1,26,44,2,4,15,32,17,3,9,14,,29,11,7],
          [1_6_2020,1578268800,1578268800000,1,46,55,5,4,11,38,16,3,2,9,26,25,17,6],
          [2_3_2020,1580688000,1580688000000,1,22,44,5,4,10,39,14,3,2,8,25,26,17,6],
          [3_2_2020,1583107200,1583107200000,1,21,15,7,4,5,31,14,6,3,2,16,28,19,9],
          [4_6_2020,1586131200,1586131200000,2,17,20,7,5,3,38,25,6,4,1,14,24,18,10],
          [5_4_2020,1588550400,1588550400000,1,16,26,8,2,6,48,27,5,4,3,15,19,22,9],
          [6_1_2020,1590969600,1590969600000,2,20,17,9,3,4,36,27,6,5,1,22,13,26,10],
          [7_6_2020,1593993600,1593993600000,10,1,11,3,6,5,31,18,8,12,4,14,20,25,2],
          [8_3_2020,1596412800,1596412800000,11,1,10,3,7,5,27,19,9,14,4,15,20,25,2],
          [9_7_2020,1599436800,1599436800000,11,4,6,2,13,5,28,3,7,20,8,12,18,38,1],
          [10_5_2020,1601856000,1601856000000,2,6,10,4,15,9,33,1,8,12,3,13,16,28,5],
          [11_6_2020,1604275200,1604275200000,3,6,14,8,11,13,22,1,12,16,5,7,17,15,2],
          [12_7_2020,1607299200,1607299200000,2,5,10,15,13,9,17,3,16,8,4,6,18,11,1],
          [1_4_2021,1609718400,1609718400000,1,4,12,17,14,8,15,5,9,10,3,7,19,11,2],
          [2_1_2021,1612137600,1612137600000,1,4,13,15,12,8,16,7,5,11,3,9,14,6,2],
          [3_1_2021,1614556800,1614556800000,1,7,11,13,16,10,4,14,6,15,2,17,8,3,5]
        ]

        const teamList = ["Astralis","BIG","Complexity","EvilGeniuses","fnatic","G2","Gambit","Heroic","Liquid","mousesports","NatusVincere","OG","Spirit","Virtus.pro","Vitality"]
        var teamStatsList = [
          ['Astralis', 40.44, 36.32, 77.09, 73.07, 1.15],
          ['BIG', 41.66, 40.46, 74.67, 70.0, 1.08],
          ['Complexity', 41.73, 40.35, 74.37, 70.88, 1.08],
          ['Evil Geniuses', 44.37, 43.64, 74.18, 71.66, 1.08],
          ['fnatic', 43.75, 43.62, 74.39, 69.28, 1.05],
          ['G2', 42.85, 41.85, 73.97, 70.02, 1.06],
          ['Gambit', 40.97, 37.43, 75.13, 72.34, 1.11],
          ['Heroic', 44.24, 42.35, 74.65, 71.09, 1.08],
          ['Liquid', 41.42, 38.68, 75.86, 72.26, 1.12],
          ['mousesports', 41.05, 39.56, 74.11, 70.2, 1.07],
          ['Natus Vincere', 42.08, 39.4, 74.89, 71.4, 1.1],
          ['OG', 44.64, 43.3, 73.16, 71.53, 1.07],
          ['Spirit', 40.33, 38.41, 74.18, 71.4, 1.09],
          ['Virtus.pro', 39.41, 39.21, 72.49, 69.19, 1.04],
          ['Vitality', 42.14, 40.17, 75.54, 71.5, 1.1]
        ]

     function insertLeft(teamName){
      
      const isTeam = (element) => element === teamName;
      teamName = teamName.replace(/\s/g, '');
      var index = teamList.findIndex(isTeam);

      document.getElementById('kills-left').textContent = teamStatsList[index][1];
      document.getElementById('deaths-left').textContent = teamStatsList[index][2];
      document.getElementById('adr-left').textContent = teamStatsList[index][3];
      document.getElementById('kda-left').textContent = teamStatsList[index][4];
      document.getElementById('rating-left').textContent = teamStatsList[index][5];

      var graph_left = [],
        dataLength = data.length,
        i = 0;
        for (i; i < dataLength; i += 1) {
          graph_left.push([
            data[i][2], // the date
            data[i][index+3], // the volume
          ]);
        }

        // Create the chart
        Highcharts.chart('graph_content_l', {
          exporting: { enabled: false },
            chart: {
              styledMode: true,
              type: 'area',},
            title: {
              text: 'Team Ranking',
              },
            yAxis: {
              title:{
                text: 'Rank',
              },
              reversed: true,
              showFirstLabel: false,
              showLastLabel: true,},
             xAxis: {
              title: {
                text: 'Date',},
                type: 'datetime',},
                plotOptions: {
                    borderWidth: 0 // < set this option
                  },

            series: [{
              showInLegend: false,
              name: 'Ranking',
              data: graph_left,
              threshold: null,}],
        });
     }

     function insertRight(teamName){
      const isTeam = (element) => element === teamName;
      teamName = teamName.replace(/\s/g, '');
      var index = teamList.findIndex(isTeam);

      document.getElementById('kills-right').textContent = teamStatsList[index][1];
      document.getElementById('deaths-right').textContent = teamStatsList[index][2];
      document.getElementById('adr-right').textContent = teamStatsList[index][3];
      document.getElementById('kda-right').textContent = teamStatsList[index][4];
      document.getElementById('rating-right').textContent = teamStatsList[index][5];

      var graph_right = [],
        dataLength = data.length,
        i = 0;
        for (i; i < dataLength; i += 1) {
          graph_right.push([
            data[i][2], // the date
            data[i][index+3], // the volume
          ]);
        }

        // Create the chart
        Highcharts.chart('graph_content_r', {
          exporting: { enabled: false },
            chart: {
              styledMode: true,
              type: 'area',},
            title: {
              text: 'Team Ranking',
              },
            yAxis: {
              title:{
                text: 'Rank',
              },
              reversed: true,
              showFirstLabel: false,
              showLastLabel: true,},
             xAxis: {
              title: {
                text: 'Date',},
                type: 'datetime',},
                plotOptions: {
                    borderWidth: 0 // < set this option
                  },

            series: [{
              showInLegend: false,
              name: 'Ranking',
              data: graph_right,
              threshold: null,}],
        });
     }
     
    </script>



  <p id="selectedBool" hidden>{{ selected }}</p>
  <p id="team1variable" hidden>{{ team1 }}</p>
  <p id="team2variable" hidden>{{ team2 }}</p>

 <div class="main">

    <div class="left">
      <div class="row">
        <div id="left-team" class="col-sm-3 side_container" style="display:none;">
          <div class="team_header1">
            <img id="team_logo_left" src="https://img-cdn.hltv.org/teamlogo/GAlByJtDTnkgbb9p_71SUL.png?ixlib=java-2.1.0&w=100&s=ddc5952ae492cbefb10fbe64471486b5" class = "team_pick" alt="Team Logo">
            <h4 id="team_name_left" class="team_name" style="margin-left:50px;">Team Name</h4>
          </div>
          <div class="col-sm-12 graph_container">
            <div id="graph_content_l"></div>
          </div>
          <div class="col-sm-12">
            <table class="table table-bordered">
              <thead>
                 <tr>
                  <td colspan="2">Team Statistics</td>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Average Kills</td>
                  <td><p id="kills-left"></p></td>
                </tr>
                <tr>
                  <td>Average Death</td>
                  <td><p id="deaths-left"></p></td>
                </tr>
                <tr>
                  <td>Average Damage</td>
                  <td><p id="adr-left"></p></td>
                </tr>
                <tr>
                  <td>Assistance Percentage</td>
                  <td><p id="kda-left"></p></td>
                </tr>
                <tr>
                  <td>Rating</td>
                  <td><p id="rating-left"></p></td>
                </tr>
              </tbody>
            </table>

          </div>
        </div>
    </div>
  </div>
    <div class="center">
      <img src="static/logo3.png" alt="" style="">
      <div class="pick">
        <div class="card" id="team1_selected">
          <p id="select_team1_text">Select team 1 below</p>
          <div class="team" id="selected1" style="display:none;">
            <img id="logo1" src="" alt="">
            <p id="team1Name">vitality</p>
          </div>
        </div>
        <div class="score">
          <p>Predicted round difference: <span>{{ prediction }}</span></p>
          <p style="font-size:50px;text-align:center;">{{score1}} - {{score2}}</p>
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

      <div id="right-team" class="col-sm-3 side_container" style="display:none;">
        <div class="team_header2">
         <img id="team_logo_right" src="https://img-cdn.hltv.org/teamlogo/9bgXHp-oh1oaXr7F0mTGmd.svg?ixlib=java-2.1.0&s=f567161ab183001be33948b98c4b20675" class = "team_pick" alt="...">
         <h4 id="team_name_right" class="team_name" style="margin-right:50px;">Team Name</h4>
       </div>
      <div class="col-sm-12 graph_container">
       <div id="graph_content_r"></div>
       </div>
      <div class="col-sm-12">
       <table class="table table-bordered">
         <thead>
            <tr>
             <td colspan="2">Team Statistics</td>
           </tr>
         </thead>
         <tbody>
                <tr>
                  <td>Average Kills</td>
                  <td><p id="kills-right"></p></td>
                </tr>
                <tr>
                  <td>Average Death</td>
                  <td><p id="deaths-right"></p></td>
                </tr>
                <tr>
                  <td>Average Damage</td>
                  <td><p id="adr-right"></p></td>
                </tr>
                <tr>
                  <td>Assistance Percentage</td>
                  <td><p id="kda-right"></p></td>
                </tr>
                <tr>
                  <td>Rating</td>
                  <td><p id="rating-right"></p></td>
                </tr>
              </tbody>
     </table>
     </div>
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
  /*document.getElementById('team_logo_left').src = logo;*/
  document.getElementById('team_name_left').textContent = team1Name;
  document.getElementById('left-team').style.display="block";
  /*document.getElementById('team_logo_right').src = logo;*/
  document.getElementById('team_name_right').textContent = team2Name;
  document.getElementById('left-team').style.display="block";
  document.getElementById('right-team').style.display="block";
  insertLeft(team1Name);
  insertRight(team2Name);
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
       document.getElementById('team_logo_left').src = logo;
       document.getElementById('team_name_left').textContent = teamName;
       document.getElementById('left-team').style.display="block";
       insertLeft(teamName);
       
     }else{
       var select_team2_text = document.getElementById('select_team2_text');
       select_team2_text.style.display = "none";
       document.getElementById('logo2').src = logo;
       document.getElementById('team2Name').textContent = teamName;
       team_container2.style.display="block";
       document.getElementById("team2input").value = teamName;
       document.getElementById('team_logo_right').src = logo;
       document.getElementById('team_name_right').textContent = teamName;
       document.getElementById('right-team').style.display="block";
       insertRight(teamName);
     }


 }



 </script>
 </body>

</html>


