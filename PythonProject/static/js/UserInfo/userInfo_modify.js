$(function () {
    setTimeout(ajaxModifyQuery,"100");
  function ajaxModifyQuery() {	
	$.ajax({
		url : "/UserInfo/update/" + $("#userInfo_user_name_modify").val(),
		type : "get",
		data : {
			//user_name : $("#userInfo_user_name_modify").val(),
		},
		beforeSend : function () {
			$.messager.progress({
				text : "正在获取中...",
			});
		},
		success : function (userInfo, response, status) {
			$.messager.progress("close");
			if (userInfo) { 
				$("#userInfo_user_name_modify").val(userInfo.user_name);
				$("#userInfo_user_name_modify").validatebox({
					required : true,
					missingMessage : "请输入用户名",
					editable: false
				});
				$("#userInfo_password_modify").val(userInfo.password);
				$("#userInfo_password_modify").validatebox({
					required : true,
					missingMessage : "请输入登录密码",
				});
				$("#userInfo_areaObj_areaId_modify").combobox({
					url:"/Area/listAll?csrfmiddlewaretoken=" + $('input[name="csrfmiddlewaretoken"]').val(),
					method: "GET",
					valueField:"areaId",
					textField:"areaName",
					panelHeight: "auto",
					editable: false, //不允许手动输入 
					onLoadSuccess: function () { //数据加载完毕事件
						$("#userInfo_areaObj_areaId_modify").combobox("select", userInfo.areaObjPri);
						//var data = $("#userInfo_areaObj_areaId_edit").combobox("getData"); 
						//if (data.length > 0) {
							//$("#userInfo_areaObj_areaId_edit").combobox("select", data[0].areaId);
						//}
					}
				});
				$("#userInfo_name_modify").val(userInfo.name);
				$("#userInfo_name_modify").validatebox({
					required : true,
					missingMessage : "请输入姓名",
				});
				$("#userInfo_sex_modify").val(userInfo.sex);
				$("#userInfo_sex_modify").validatebox({
					required : true,
					missingMessage : "请输入性别",
				});
				$("#userInfo_userPhotoImgMod").attr("src", userInfo.userPhoto);
				$("#userInfo_birthday_modify").datebox({
					value: userInfo.birthday,
					required: true,
					showSeconds: true,
				});
				$("#userInfo_telephone_modify").val(userInfo.telephone);
				$("#userInfo_telephone_modify").validatebox({
					required : true,
					missingMessage : "请输入联系电话",
				});
				$("#userInfo_address_modify").val(userInfo.address);
				$("#userInfo_address_modify").validatebox({
					required : true,
					missingMessage : "请输入家庭地址",
				});
			} else {
				$.messager.alert("获取失败！", "未知错误导致失败，请重试！", "warning");
				$(".messager-window").css("z-index",10000);
			}
		}
	});

  }

	$("#userInfoModifyButton").click(function(){ 
		if ($("#userInfoModifyForm").form("validate")) {
			$("#userInfoModifyForm").form({
			    url:"UserInfo/update/" + $("#userInfo_user_name_modify").val(),
			    onSubmit: function(){
					if($("#userInfoEditForm").form("validate"))  {
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
			$("#userInfoModifyForm").submit();
		} else {
			$.messager.alert("错误提示","你输入的信息还有错误！","warning");
			$(".messager-window").css("z-index",10000);
		}
	});
});
