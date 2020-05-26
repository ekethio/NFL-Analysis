NFL Predictive Model

Possible features that determine the strength of a team:<br/>
(Note: Each sub-list includes factors in decreasing value of importance.)<br/>
	<ol> 
	<li>Offense:</li>
		<ul>
	 <li>Individual components of the offense:</li>
               <ul>
		  <li>Quarterback's efficiency.</li>
		  <li>Offensive play calling.</li>
		   <li> Offensive line (Pass and Run block)</li>
		   <li>kill position players. </li>
		</ul>
	 <li> Ways to estimate offensive efficiency:</li>
	        <ul>
		  <li>Yards gained per play/drive/game</li>
		  <li>Points scored per drive/game</li>
		  <li>Percentage of plays that are successful.</li>
		  <li>Explosive plays (possibly helpful to account for luck).</li>
		  <li>Efficiency and playcalling on high-leverage plays.</li>
		  <li>The likelihood of scoring without converting a high leveraged play.</li>
	        </ul>
		<li>Ways to account for offensive luck: </li>
		<ul>
		  <li>Plays, drives, and games decided by unsustainable explosive plays.</li> 
		  <li>Penalties that changed the outcome of a play.</li>
		  <li>Unsustainable bad/good luck on high leveraged plays. </li>
			</ul>
	  <li>Ways to account for offensive output that is driven by game script:<li/>
		<ul>
		  <li>Discounting garbage time performance(including when trailing signficantly).</li>
		  <li>Discounting end of half/game plays, hail marys,  or any inconsequential plays </li>
		   to the outcome of a game. 
		</ul>
	</ul>
	<li> Defense:</li>
	 	<ul>
		<li>Individual components of the defense: </li>
		 <ul>
		  <li>Defensive play calling.</li>
		  <li>Defnsive line.</li>
		  <li>Secondary.</li>
		  <li>Linebacking core.</li>
			</ul>
		<li>Ways to estimate defensive efficiency: </li>
		<ul>
		  <li>Yards allowed per play/drive/game.</li>
		  <li>points allowed per drive/game.</li>
		  <li>Percentage of plays allowed that are successful. </li>
		  <li>Explosive plays allowed.</li>
		  <li>Efficiency on high leveraged plays. </li>	
	      	  <li>First half, and 4th quarter splits (to account for endurance.)</li>
		  <li>Amount of constant pressure put on QB. </li>
		  <li>Frequency of pushing opponent to high leveraged plays.</li>
		 </ul>
		<li>Ways to account for defensive luck:</li>
		<ul>
		  <li>Interceptions, or explosive plays allowed. </li>
		  <li>Penalities that changed the outcome of a play. </li>
		  <li>Unsustainable good luck on high-leveraged plays. </li>
		 </ul
		<li>Ways to account from defensive performance driven by game sript:</li>
		<ul>
		  <li>Discounting garbage time performance(indluing ahead or trailing by significanly).</li>
		  <li>Discounting end of half/game, or other plays that aren't significant to the </li>
		   outocme of the footbale game.
			</ul>
	</ol>	   
		  
			
		    
		   
		   
			
		
		  
		  
		  
		  
		 
