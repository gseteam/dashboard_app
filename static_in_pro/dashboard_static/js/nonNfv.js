/**
 * Created by jaiswroh on 9/5/2016.
 */
 $(document).ready(function() {
      $('#nonnfv1').one('click', function( onclick ){
    $.post({
        url: "/gettype1",
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
                $('#nonnfv').append('<li><a href=\"activity_detail/'+arr[j]+'\">'+arr[j]+'</a></li>');
           }

		}
    })

} )
	} )
