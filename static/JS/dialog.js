{% if messages  %}
    <script>
       $(document).ready(function(){
         {% for msg in messages %}
         // 把Django返回的消息内容更新为模态框的内容 通过id号查找
            $("#messageModal").find("#message-body").html('{{ msg.message }}');
          // 显示模态框
            $("#messageModal").modal('show');
         {% endfor %}
       });
    </script>
{% endif %}
