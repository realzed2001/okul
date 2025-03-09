#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <FS.h>

const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASSWORD";

ESP8266WebServer server(80);

void setup() {
    Serial.begin(115200);
    if (!SPIFFS.begin()) {
        Serial.println("Failed to mount file system");
        return;
    }

    WiFi.begin(ssid, password);
    Serial.print("Connecting to WiFi...");
    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.print(".");
    }
    Serial.println("Connected!");

    server.on("/", HTTP_GET, handleRoot);
    server.on("/submit", HTTP_POST, handlePost);
    server.begin();
    Serial.println("HTTP server started");
}

void handleRoot() {
    server.send(200, "text/html", "<form action=\"/submit\" method=\"POST\"><input type=\"text\" name=\"data\"><input type=\"submit\" value=\"Submit\"></form>");
}

void handlePost() {
    if (server.hasArg("data")) {
        String data = server.arg("data");
        File file = SPIFFS.open("/bilgi.txt", "a");
        if (!file) {
            server.send(500, "text/plain", "Failed to open file for writing");
            return;
        }
        file.println(data);
        file.close();
        server.send(200, "text/plain", "Data received and saved");
    } else {
        server.send(400, "text/plain", "Bad Request");
    }
}

void loop() {
    server.handleClient();
}