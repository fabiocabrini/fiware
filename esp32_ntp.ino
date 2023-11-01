#include <WiFi.h>

#define NTP_SERVER     "ip_ntp_server"
#define UTC_OFFSET     0
#define UTC_OFFSET_DST 0

void printLocalTime() {
  struct tm timeinfo;
  if (!getLocalTime(&timeinfo)) {
    Serial.println("Connection Err");
    return;
  }

  // Ajustar o deslocamento horário para UTC -3 (AST/BRT)
  timeinfo.tm_hour -= 3;
  if (timeinfo.tm_hour < 0) {
    timeinfo.tm_hour += 24;  // Garantir que o valor de hora seja positivo
  }

  Serial.println(&timeinfo, "%H:%M:%S");
  Serial.println(&timeinfo, "%d/%m/%Y   %Z");
}

void setup() {
  Serial.begin(115200);
  Serial.println("Connecting to ");
  Serial.print("WiFi ");
  WiFi.begin("ssid", "password", 6);
  while (WiFi.status() != WL_CONNECTED) {
    delay(250);
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  Serial.println("Online");
  Serial.println("Updating time...");
  configTime(UTC_OFFSET, UTC_OFFSET_DST, NTP_SERVER);
}

void loop() {
  printLocalTime();
  delay(250);
}
