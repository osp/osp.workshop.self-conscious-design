$(document).ready(function(){
     
    //$("#theText").html(function(i, oldHTML) {
	//console.log (oldHTML.replace(/ /g, '</span><span class="word separated effacer">'));
        //return oldHTML.replace(/ /g, '</span><span class="word separated effacer">');
    //});
    $("#theText").html('<span class="word separated effacer">' + $("#theText span").html().replace(/ /g, '</span><span class="word separated effacer">') + '</span>'); 
    
    var delay1 = 200;
    var delay2 = 400;
    var $words = $('.word');
    
    $words.each(function (i){
        
        var myElement = $words[i];
        
        setTimeout(function(){
            
         
            $(myElement).addClass('effacer');
            
        }, i*delay2 + 4000);
        
         setTimeout(function(){
          
            $(myElement).removeClass('separated');
            
        }, i*delay2 + 3000);
        
        setTimeout(function(){
          
            $(myElement).removeClass('effacer');
            
        }, i*delay2 + 1000);
        
        
            
    });

	$('#theDescription').click(function(){

		$('#theDescription').html('<span class="word separated effacer">' + $("#theText span").html().replace(/ /g, '</span><span class="word separated effacer">') + '</span>'); 
    
    var delay1 = 200;
    var delay2 = 400;
    var $words = $('.word');
    
    $words.each(function (i){
        
        var myElement = $words[i];
        
        setTimeout(function(){
            
         
            $(myElement).addClass('effacer');
            
        }, i*delay2 + 4000);
        
         setTimeout(function(){
          
            $(myElement).removeClass('separated');
            
        }, i*delay2 + 3000);
        
        setTimeout(function(){
          
            $(myElement).removeClass('effacer');
            
        }, i*delay2 + 1000);
        
        
            
    });
	



	});
    
});
