$(function () {
    setTimeout(ajaxModifyQuery,"100");
  function ajaxModifyQuery() {	
	$.ajax({
		url : "/Claim/update/" + $("#claim_claimId_modify").val(),
		type : "get",
		data : {
			//claimId : $("#claim_claimId_modify").val(),
		},
		beforeSend : function () {
			$.messager.progress({
				text : "正在获取中...",
			});
		},
		success : function (claim, response, status) {
			$.messager.progress("close");
			if (claim) { 
				$("#claim_claimId_modify").val(claim.claimId);
				$("#claim_claimId_modify").validatebox({
					required : true,
					missingMessage : "请输入认领id",
					editable: false
				});
				$("#claim_lostFoundObj_lostFoundId_modify").combobox({
					url:"/LostFound/listAll?csrfmiddlewaretoken=" + $('input[name="csrfmiddlewaretoken"]').val(),
					method: "GET",
					valueField:"lostFoundId",
					textField:"title",
					panelHeight: "auto",
					editable: false, //不允许手动输入 
					onLoadSuccess: function () { //数据加载完毕事件
						$("#claim_lostFoundObj_lostFoundId_modify").combobox("select", claim.lostFoundObjPri);
						//var data = $("#claim_lostFoundObj_lostFoundId_edit").combobox("getData"); 
						//if (data.length > 0) {
							//$("#claim_lostFoundObj_lostFoundId_edit").combobox("select", data[0].lostFoundId);
						//}
					}
				});
				$("#claim_personName_modify").val(claim.personName);
				$("#claim_personName_modify").validatebox({
					required : true,
					missingMessage : "请输入认领人",
				});
				$("#claim_claimTime_modify").datetimebox({
					value: claim.claimTime,
					required: true,
					showSeconds: true,
				});
				$("#claim_contents_modify").val(claim.contents);
				$("#claim_addTime_modify").val(claim.addTime);
			} else {
				$.messager.alert("获取失败！", "未知错误导致失败，请重试！", "warning");
				$(".messager-window").css("z-index",10000);
			}
		}
	});

  }

	$("#claimModifyButton").click(function(){ 
		if ($("#claimModifyForm").form("validate")) {
			$("#claimModifyForm").form({
			    url:"Claim/update/" + $("#claim_claimId_modify").val(),
			    onSubmit: function(){
					if($("#claimEditForm").form("validate"))  {
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
			$("#claimModifyForm").submit();
		} else {
			$.messager.alert("错误提示","你输入的信息还有错误！","warning");
			$(".messager-window").css("z-index",10000);
		}
	});
});
