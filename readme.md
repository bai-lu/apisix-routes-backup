# apisix 路由备份恢复脚本

从 apisix dashboard 获取路由列表, 保存之 routes.json, 执行脚本, 修改域名, 认证等参数进行恢复

仅恢复路由, 不支持恢复其他配置(如证书, 插件, 服务)

## 指定恢复的 apisix 及 恢复路由文件

创建环境变量

```
export APISIX_ADMIN_URL="https://ad.example.com/apisix/admin/routes"
export ROUTES_BACKUP_FILE="routes.json"
```

## headers 获取

部分访问 apisix-dashboards 从 chrome 开发者模式复制(fetch格式)

## plugins

自定义插件, 增加官方版本不支持的场景
