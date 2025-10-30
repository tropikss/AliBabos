FROM maven:3.9.9-eclipse-temurin-21 AS build
WORKDIR /workspace/app
COPY pom.xml .
COPY src ./src
RUN mvn -B -DskipTests package

# --- Étape d'exécution (JRE 21, non-root) ---
FROM eclipse-temurin:21-jre
WORKDIR /app
RUN useradd -r -u 1001 spring && mkdir -p /app && chown -R spring:spring /app
ENV SPRING_PROFILES_ACTIVE=default
ENV JAVA_OPTS="-XX:MaxRAMPercentage=75 -XX:InitialRAMPercentage=50"
COPY --from=build /workspace/app/target/*.jar /app/app.jar
USER spring
EXPOSE 8080
ENTRYPOINT ["sh","-c","java $JAVA_OPTS -jar /app/app.jar"]