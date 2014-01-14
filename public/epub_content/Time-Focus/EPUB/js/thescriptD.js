$(document).ready(function(){
   
	var once = false;  
    
	$('#theDescription').click(function(){
	
	if(once == false){

		$('#theDescription').html('<span class="word">' + $("#theDescription span").html().replace(/ /g, '</span><span class="word">') + '</span>'); 
    
   		var delay1 = 200;
    		var delay2 = 400;
    		var $words = $('.word');
    
    		$words.each(function (i){
        
       		var myElement = $words[i];
        
        	setTimeout(function(){
            
         
            		$(myElement).addClass('effacer');
            
        	}, i*delay2 + 4000);
        
         
            
    		});
		
		once = true;

	}

	



	});
    
});
