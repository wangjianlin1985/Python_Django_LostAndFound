$(function () {
    setTimeout(ajaxModifyQuery,"100");
  function ajaxModifyQuery() {	
	$.ajax({
		url : "/Praise/update/" + $("#praise_praiseId_modify").val(),
		type : "get",
		data : {
			//praiseId : $("#praise_praiseId_modify").val(),
		},
		beforeSend : function () {
			$.messager.progress({
				text : "正在获取中...",
			});
		},
		success : function (praise, response, status) {
			$.messager.progress("close");
			if (praise) { 
				$("#praise_praiseId_modify").val(praise.praiseId);
				$("#praise_praiseId_modify").validatebox({
					required : true,
					missingMessage : "请输入表扬id",
					editable: false
				});
				$("#praise_lostFoundObj_lostFoundId_modify").combobox({
					url:"/LostFound/listAll?csrfmiddlewaretoken=" + $('input[name="csrfmiddlewaretoken"]').val(),
					method: "GET",
					valueField:"lostFoundId",
					textField:"title",
					panelHeight: "auto",
					editable: false, //不允许手动输入 
					onLoadSuccess: function () { //数据加载完毕事件
						$("#praise_lostFoundObj_lostFoundId_modify").combobox("select", praise.lostFoundObjPri);
						//var data = $("#praise_lostFoundObj_lostFoundId_edit").combobox("getData"); 
						//if (data.length > 0) {
							//$("#praise_lostFoundObj_lostFoundId_edit").combobox("select", data[0].lostFoundId);
						//}
					}
				});
				$("#praise_title_modify").val(praise.title);
				$("#praise_title_modify").validatebox({
					required : true,
					missingMessage : "请输入标题",
				});
				$("#praise_contents_modify").val(praise.contents);
				$("#praise_contents_modify").validatebox({
					required : true,
					missingMessage : "请输入表扬内容",
				});
				$("#praise_addTime_modify").datetimebox({
					value: praise.addTime,
					required: true,
					showSeconds: true,
				});
			} else {
				$.messager.alert("获取失败！", "未知错误导致失败，请重试！", "warning");
				$(".messager-window").css("z-index",10000);
			}
		}
	});

  }

	$("#praiseModifyButton").click(function(){ 
		if ($("#praiseModifyForm").form("validate")) {
			$("#praiseModifyForm").form({
			    url:"Praise/update/" + $("#praise_praiseId_modify").val(),
			    onSubmit: function(){
					if($("#praiseEditForm").form("validate"))  {
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
			$("#praiseModifyForm").submit();
		} else {
			$.messager.alert("错误提示","你输入的信息还有错误！","warning");
			$(".messager-window").css("z-index",10000);
		}
	});
});
