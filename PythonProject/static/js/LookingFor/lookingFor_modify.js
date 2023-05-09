$(function () {
    setTimeout(ajaxModifyQuery,"100");
  function ajaxModifyQuery() {	
	$.ajax({
		url : "/LookingFor/update/" + $("#lookingFor_lookingForId_modify").val(),
		type : "get",
		data : {
			//lookingForId : $("#lookingFor_lookingForId_modify").val(),
		},
		beforeSend : function () {
			$.messager.progress({
				text : "正在获取中...",
			});
		},
		success : function (lookingFor, response, status) {
			$.messager.progress("close");
			if (lookingFor) { 
				$("#lookingFor_lookingForId_modify").val(lookingFor.lookingForId);
				$("#lookingFor_lookingForId_modify").validatebox({
					required : true,
					missingMessage : "请输入寻物id",
					editable: false
				});
				$("#lookingFor_title_modify").val(lookingFor.title);
				$("#lookingFor_title_modify").validatebox({
					required : true,
					missingMessage : "请输入标题",
				});
				$("#lookingFor_goodsName_modify").val(lookingFor.goodsName);
				$("#lookingFor_goodsName_modify").validatebox({
					required : true,
					missingMessage : "请输入丢失物品",
				});
				$("#lookingFor_goodsPhotoImgMod").attr("src", lookingFor.goodsPhoto);
				$("#lookingFor_lostTime_modify").datetimebox({
					value: lookingFor.lostTime,
					required: true,
					showSeconds: true,
				});
				$("#lookingFor_lostPlace_modify").val(lookingFor.lostPlace);
				$("#lookingFor_lostPlace_modify").validatebox({
					required : true,
					missingMessage : "请输入丢失地点",
				});
				$("#lookingFor_goodDesc_modify").val(lookingFor.goodDesc);
				$("#lookingFor_goodDesc_modify").validatebox({
					required : true,
					missingMessage : "请输入物品描述",
				});
				$("#lookingFor_reward_modify").val(lookingFor.reward);
				$("#lookingFor_reward_modify").validatebox({
					required : true,
					missingMessage : "请输入报酬",
				});
				$("#lookingFor_telephone_modify").val(lookingFor.telephone);
				$("#lookingFor_telephone_modify").validatebox({
					required : true,
					missingMessage : "请输入联系电话",
				});
				$("#lookingFor_userObj_user_name_modify").combobox({
					url:"/UserInfo/listAll?csrfmiddlewaretoken=" + $('input[name="csrfmiddlewaretoken"]').val(),
					method: "GET",
					valueField:"user_name",
					textField:"name",
					panelHeight: "auto",
					editable: false, //不允许手动输入 
					onLoadSuccess: function () { //数据加载完毕事件
						$("#lookingFor_userObj_user_name_modify").combobox("select", lookingFor.userObjPri);
						//var data = $("#lookingFor_userObj_user_name_edit").combobox("getData"); 
						//if (data.length > 0) {
							//$("#lookingFor_userObj_user_name_edit").combobox("select", data[0].user_name);
						//}
					}
				});
				$("#lookingFor_addTime_modify").val(lookingFor.addTime);
			} else {
				$.messager.alert("获取失败！", "未知错误导致失败，请重试！", "warning");
				$(".messager-window").css("z-index",10000);
			}
		}
	});

  }

	$("#lookingForModifyButton").click(function(){ 
		if ($("#lookingForModifyForm").form("validate")) {
			$("#lookingForModifyForm").form({
			    url:"LookingFor/update/" + $("#lookingFor_lookingForId_modify").val(),
			    onSubmit: function(){
					if($("#lookingForEditForm").form("validate"))  {
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
			$("#lookingForModifyForm").submit();
		} else {
			$.messager.alert("错误提示","你输入的信息还有错误！","warning");
			$(".messager-window").css("z-index",10000);
		}
	});
});
