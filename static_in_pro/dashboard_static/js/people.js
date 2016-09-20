/**
 * Created by jaiswroh on 9/5/2016.
 */
$(document).ready(function() {
      $('#people').one('click', function( onclick ){
    $.post({
        url: "/getvalues",
        data : {},
        success : function(json) {
			 //alert(json);

	  		console.log(JSON.stringify(json));


           //var t = JSON.stringify(json);
		   var t= jQuery.parseJSON(JSON.stringify(json))
			var arr=[];
			for (var i in t){
			  arr.push(t[i]);
			}
            arr.sort();
			//alert(arr);
			console.log(arr);
			for (var j in arr){
                var k=arr[j];
                $('#menu').append('<li><a href=\"people_detail/'+arr[j]+'\">'+arr[j]+'</a></li>');
           }
			
		}
    })
	
} )
	} )