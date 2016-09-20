/**
 * Created by jaiswroh on 9/6/2016.
 */
    $(document).ready(function() {

    $.post({
        url: "/Remove_people_detail",
        data : {},
        success : function(json) {
			 //alert(json);
             //$("#select-from").find('option').remove();
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
                $('#select-from').append('<option>'+arr[j]+'</option>');
           }

		}
    })

} )


    $(document).ready(function() {

    $.post({
        url: "/Add_people_detail",
        data : {},
        success : function(json) {
			 //alert(json);
             //$("#select-to").find('option').remove();
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
                $('#select-to').append('<option>'+arr[j]+'</option>');
           }

		}
    })

} )

     $(document).ready(function () {
         //alert("i m at ready")
    $('#input').click(function () {
        //alert("i m at submit call")
        $('#select-to option').each(function () {
            //alert($(this).text());
            $(this).prop("selected",true);
        });
                $('#select-from option').each(function () {
                    //alert($(this).text());
                    $(this).prop("selected",true);
        });
    });
});
 
    $(document).ready(function() {
        var act_name=$('#name').val()

        $('#delete').click('click',function(onclick) {


            var result=confirm("Want to delete this Activity ?");
            if(result){

                $.post({
                     url: "/delete_activity_detail/"+act_name+"/",
                    data : {},
                   success : function() {
                   window.location='/home';
            }



		})
    }
})
} )
