/**
 * Created by jaiswroh on 9/6/2016.
 */
   $(document).ready(function() {
        //alert('i m here');
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
                $('#abc').append('<option>'+arr[j]+'</option>');
           }

		}
    })

} )


    $(document).ready(function() {

 $('#msgbx_err').css('display','none');
      $('#save').click('click',function(){

          $('#header').remove();
          var name=$('#name').val();

          var type=$('#type').val();
    $.post({

        url: "/activity_check_availability/"+name+"/"+type+"/",
        data : {},
        async: false,
        success : function(json) {
            //alert(json);
            console.log(JSON.stringify(json));
           //var t = JSON.stringify(json);
            var t = jQuery.parseJSON(JSON.stringify(json))
            var arr = [];
            for (var i in t) {
                arr.push(t[i]);
            }
            //alert(arr);
            console.log(arr);
            if (arr[0] == "1") {
                $('#msgbx_err').css('display', 'block');
                $('#name_status').html('ERROR:'+name+' is exists in database. please type another activity name');
            }
            else{
                $('#msgbx_err').css('display', 'none');
                 $('#name_status').html("");
            }
        }
    })

} )
	} )

     function checkfun() {
            //alert("i m in fun");
            var check=document.getElementById("name_status").innerHTML;
            if (check){
                return false
            }

            else{
                return true;
            }

        }