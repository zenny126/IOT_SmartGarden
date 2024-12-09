#include <ESP8266WiFi.h>
#include <WebSocketsServer.h>
#include <DHT.h>

const char *ssid = "Duong2G";
const char *password = "ngocanh286";
const int ledPin = D1;         // Chân GPIO1 (D1) được sử dụng cho kênh đèn của module relay
const int pumpPin = D2;        // Chân GPIO2 (D2) được sử dụng cho kênh máy bơm của module relay
const int dhtPin = D3;         // Chân GPIO3 (D3) được sử dụng cho cảm biến DHT11
const int soilDigitalPin = D0; // Chân GPIO0 (D0) được sử dụng cho cảm biến độ ẩm đất (Digital Output)
const int soilAnalogPin = A0;  // Chân A0 được sử dụng cho cảm biến độ ẩm đất (Analog Output)
const int relayOn = LOW;       // Tín hiệu kích hoạt kênh relay
const int relayOff = HIGH;     // Tín hiệu ngắt kênh relay

bool autoWateringEnabled = false;    // Trạng thái chế độ tự động tưới nước
const int desiredMoistureLevel = 60; // Đặt mức độ ẩm đất mong muốn tại đây

DHT dht(dhtPin, DHT11);
WebSocketsServer webSocket = WebSocketsServer(81);

void startWebSocket()
{
    webSocket.begin();
    webSocket.onEvent(webSocketEvent);
}

void webSocketEvent(uint8_t num, WStype_t type, uint8_t *payload, size_t length)
{
    switch (type)
    {
    case WStype_TEXT:
        Serial.printf("[%u] get text: %s\n", num, payload);
        String message = (char *)payload;
        webSocket.sendTXT(num, payload); // Thông báo nội dung nhận được cho client
        if (message == "on")
        {
            digitalWrite(ledPin, relayOn); // Bật đèn khi nhận tin "on"
            webSocket.broadcastTXT("Hi All! LED is turned ON");
            // Thông báo trạng thái bật đèn cho tất cả client đang kết nối
        }
        else if (message == "off")
        { // Tắt đèn khi nhận tin "off"
            digitalWrite(ledPin, relayOff);
            webSocket.broadcastTXT("Hi All! LED is turned OFF");
            // Thông báo trạng thái tắt đèn cho tất cả client đang kết nối
        }
        else if (message == "pump_on")
        {
            digitalWrite(pumpPin, relayOn); // Bật máy bơm khi nhận tin "pump_on"
            webSocket.broadcastTXT("Hi All! Pump is turned ON");
            // Thông báo trạng thái bật máy bơm cho tất cả client đang kết nối
        }
        else if (message == "pump_off")
        { // Tắt máy bơm khi nhận tin "pump_off"
            digitalWrite(pumpPin, relayOff);
            webSocket.broadcastTXT("Hi All! Pump is turned OFF");
            // Thông báo trạng thái tắt máy bơm cho tất cả client đang kết nối
        }
        else if (message == "auto_on")
        {
            autoWateringEnabled = true; // Bật chế độ tự động tưới nước
            webSocket.broadcastTXT("Hi All! Auto watering is turned ON");
            // Thông báo trạng thái bật chế độ tự động tưới nước cho tất cả client đang kết nối
        }
        else if (message == "auto_off")
        {
            autoWateringEnabled = false; // Tắt chế độ tự động tưới nước
            webSocket.broadcastTXT("Hi All! Auto watering is turned OFF");
            // Thông báo trạng thái tắt chế độ tự động tưới nước cho tất cả client đang kết nối
        }
        break;
    }
}

void setup()
{
    Serial.begin(115200);
    pinMode(ledPin, OUTPUT);
    pinMode(pumpPin, OUTPUT);
    digitalWrite(ledPin, relayOff);
    digitalWrite(pumpPin, relayOff);

    dht.begin();

    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(1000);
        Serial.println("Connecting to WiFi...");
    }

    Serial.println("Connected to WiFi");
    Serial.print("IP address: ");
    Serial.println(WiFi.localIP());

    startWebSocket();
}

void loop()
{
    webSocket.loop();

    // Đọc nhiệt độ và độ ẩm từ cảm biến DHT11
    float temperature = dht.readTemperature();
    float humidity = dht.readHumidity();

    // Đọc độ ẩm đất (Digital Output)
    int soilDigital = digitalRead(soilDigitalPin);

    // Độ ẩm đất (Analog Output)
    int soilAnalog = analogRead(soilAnalogPin);

    // Chuyển độ ẩm đất từ giátrị analog sang tỉ lệ phần trăm
    float soilMoisture = map(soilAnalog, 0, 1023, 0, 100);

    // Chuẩn bị dữ liệu để gửi lên client
    String data = String(temperature) + "," + String(humidity) + "," + String(soilMoisture);
    webSocket.broadcastTXT(data);

    // Kiểm tra trạng thái chế độ tự động tưới nước và thực hiện hành động tương ứng
    if (autoWateringEnabled == true)
    {
        webSocket.broadcastTXT("Auto on");
        if (soilMoisture < desiredMoistureLevel)
        {
            digitalWrite(pumpPin, relayOn); // Bật máy bơm
        }
        else
        {
            digitalWrite(pumpPin, relayOff);
        }
    }
    else {
      webSocket.broadcastTXT("Auto off");
    }

    delay(2000); // Đợi 2 giây trước khi đọc dữ liệu lại
}
