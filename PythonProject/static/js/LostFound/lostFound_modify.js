$(function () {
    setTimeout(ajaxModifyQuery,"100");
  function ajaxModifyQuery() {	
	$.ajax({
		url : "/LostFound/update/" + $("#lostFound_lostFoundId_modify").val(),
		type : "get",
		data : {
			//lostFoundId : $("#lostFound_lostFoundId_modify").val(),
		},
		beforeSend : function () {
			$.messager.progress({
				text : "正在获取中...",
			});
		},
		success : function (lostFound, response, status) {
			$.messager.progress("close");
			if (lostFound) { 
				$("#lostFound_lostFoundId_modify").val(lostFound.lostFoundId);
				$("#lostFound_lostFoundId_modify").validatebox({
					required : true,
					missingMessage : "请输入招领id",
					editable: false
				});
				$("#lostFound_title_modify").val(lostFound.title);
				$("#lostFound_title_modify").validatebox({
					required : true,
					missingMessage : "请输入标题",
				});
				$("#lostFound_goodsName_modify").val(lostFound.goodsName);
				$("#lostFound_goodsName_modify").validatebox({
					required : true,
					missingMessage : "请输入物品名称",
				});
				$("#lostFound_pickUpTime_modify").datetimebox({
					value: lostFound.pickUpTime,
					required: true,
					showSeconds: true,
				});
				$("#lostFound_pickUpPlace_modify").val(lostFound.pickUpPlace);
				$("#lostFound_pickUpPlace_modify").validatebox({
					required : true,
					missingMessage : "请输入拾得地点",
				});
				$("#lostFound_contents_modify").val(lostFound.contents);
				$("#lostFound_contents_modify").validatebox({
					required : true,
					missingMessage : "请输入描述说明",
				});
				$("#lostFound_userObj_user_name_modify").combobox({
					url:"/UserInfo/listAll?csrfmiddlewaretoken=" + $('input[name="csrfmiddlewaretoken"]').val(),
					method: "GET",
					valueField:"user_name",
					textField:"name",
					panelHeight: "auto",
					editable: false, //不允许手动输入 
					onLoadSuccess: function () { //数据加载完毕事件
						$("#lostFound_userObj_user_name_modify").combobox("select", lostFound.userObjPri);
						//var data = $("#lostFound_userObj_user_name_edit").combobox("getData"); 
						//if (data.length > 0) {
							//$("#lostFound_userObj_user_name_edit").combobox("select", data[0].user_name);
						//}
					}
				});
				$("#lostFound_phone_modify").val(lostFound.phone);
				$("#lostFound_phone_modify").validatebox({
					required : true,
					missingMessage : "请输入联系电话",
				});
				$("#lostFound_addTime_modify").val(lostFound.addTime);
			} else {
				$.messager.alert("获取失败！", "未知错误导致失败，请重试！", "warning");
				$(".messager-window").css("z-index",10000);
			}
		}
	});

  }

	$("#lostFoundModifyButton").click(function(){ 
		if ($("#lostFoundModifyForm").form("validate")) {
			$("#lostFoundModifyForm").form({
			    url:"LostFound/update/" + $("#lostFound_lostFoundId_modify").val(),
			    onSubmit: function(){
					if($("#lostFoundEditForm").form("validate"))  {
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
			$("#lostFoundModifyForm").submit();
		} else {
			$.messager.alert("错误提示","你输入的信息还有错误！","warning");
			$(".messager-window").css("z-index",10000);
		}
	});
});
