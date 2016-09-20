/**
 * Created by jaiswroh on 9/6/2016.
 */
  $(document).ready(function() {

    $.post({
        url: "/getactivity",
        data : {},
        success : function(json) {
			 //alert(json);
             //$("#len").find('option').remove();
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
                $('#len').append('<option>'+arr[j]+'</option>');
           }

		}
    })

} )

    $(document).ready(function() {
       $('#msgbx_err').css('display','none');
      $('#save').click('click', function(){
          var name=$('#check_name').val()

    $.post({

        url: "/check_availability/"+name+"/",
        data : {},
        async: false,
        success : function(json) {
            //alert(json);
            console.log(JSON.stringify(json));
    ;        //var t = JSON.stringify(json);
            var t = jQuery.parseJSON(JSON.stringify(json))
            var arr = [];
            for (var i in t) {
                arr.push(t[i]);
            }
            //alert(arr);
            console.log(arr);
            if (arr[0] == "1") {
                $('#msgbx_err').css('display', 'block');
                $('#name_status').html('ERROR:'+name+' is exists in database. please type another username');
            }
            else{
                $('#msgbx_err').css('display','none')
                $('#name_status').html("");
            }
        }
    })

} )
	} )

        function checkfun() {
            var check=document.getElementById("name_status").innerHTML;
            if (check){
                return false;

            }

            else{
                return true;
            }


        }