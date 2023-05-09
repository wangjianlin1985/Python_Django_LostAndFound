$(function () {
    setTimeout(ajaxModifyQuery,"100");
  function ajaxModifyQuery() {	
	$.ajax({
		url : "/Area/update/" + $("#area_areaId_modify").val(),
		type : "get",
		data : {
			//areaId : $("#area_areaId_modify").val(),
		},
		beforeSend : function () {
			$.messager.progress({
				text : "正在获取中...",
			});
		},
		success : function (area, response, status) {
			$.messager.progress("close");
			if (area) { 
				$("#area_areaId_modify").val(area.areaId);
				$("#area_areaId_modify").validatebox({
					required : true,
					missingMessage : "请输入区域id",
					editable: false
				});
				$("#area_areaName_modify").val(area.areaName);
				$("#area_areaName_modify").validatebox({
					required : true,
					missingMessage : "请输入区域名称",
				});
			} else {
				$.messager.alert("获取失败！", "未知错误导致失败，请重试！", "warning");
				$(".messager-window").css("z-index",10000);
			}
		}
	});

  }

	$("#areaModifyButton").click(function(){ 
		if ($("#areaModifyForm").form("validate")) {
			$("#areaModifyForm").form({
			    url:"Area/update/" + $("#area_areaId_modify").val(),
			    onSubmit: function(){
					if($("#areaEditForm").form("validate"))  {
	                	$.messager.progress({
							text : "正在提交数据中...",
						});
	                	return true;
	                } else {
	                    return false;
	                }
			    },
			    success:function(data){
			    	$.messager.progress("close");
                	var obj = jQuery.parseJSON(data);
                    if(obj.success){
                        $.messager.alert("消息","信息修改成功！");
                        $(".messager-window").css("z-index",10000);
                        //location.href="frontlist";
                    }else{
                        $.messager.alert("消息",obj.message);
                        $(".messager-window").css("z-index",10000);
                    } 
			    }
			});
			//提交表单
			$("#areaModifyForm").submit();
		} else {
			$.messager.alert("错误提示","你输入的信息还有错误！","warning");
			$(".messager-window").css("z-index",10000);
		}
	});
});
