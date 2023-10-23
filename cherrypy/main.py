import cherrypy


class DataReceiver:

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def api_data(self):
        data = cherrypy.request.json
        # 在这里编写处理来自DeviceHive插件的数据的逻辑
        # 可以对数据进行验证、处理、存储等操作
        # 这里只是一个简单的示例，将数据打印到控制台上
        print("Received data:", data)
        if data["gpu_temperature"] >= 68:
            return {"message": "gpu temp too high"}
        else:
            return {"message": "gpu temp is ok"}


if __name__ == "__main__":
    cherrypy.tree.mount(DataReceiver(), "/api")
    cherrypy.config.update({"server.socket_host": "0.0.0.0", "server.socket_port": 8000})
    cherrypy.engine.start()
    cherrypy.engine.block()
