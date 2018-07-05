$.ajax({

           type: "POST",

           url: "/task",


 　　//我们用text格式接收

　　 //dataType: "text",

　　//json格式接收数据

           dataType: "json",

           data:  "ruleId="+ruleId+"&ruleGroupId="+ruleGroupId+"&prodName="+prodName,

           success: function (jsonStr) {

 　　　　//实例2个字符串变量来拼接下拉列表

　　　　 //alert(jsonStr);

　　　　 //使用jquery解析json中的数据

               var ruleListTemp = "<table width=\"100%\"  border=\"0\" cellspacing=\"0\" cellpadding=\"0\">";

                $.each(jsonStr, function (n, value) {

 　　　　　　//alert(value.ruleId);

                   ruleListTemp += ("<tr><td>" + value.ruleName);

                   ruleListTemp += ("</td></tr>");

               });

                ruleListTemp += ("</table>");

               $("#ruleList").html(ruleListTemp);

           }

    });