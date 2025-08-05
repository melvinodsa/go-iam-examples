package main

import (
	"fmt"
	"log"
	"strings"

	"github.com/gofiber/fiber/v2"
	goiam "github.com/melvinodsa/go-iam-sdk/golang"
)

const (
	baseUrl      = "http://localhost:3000"
	clientId     = "abcdef1234567890abcdef1234567890"
	clientSecret = "abcdef1234567890abcdef1234567890"
)

func main() {
	app := fiber.New()

	service := goiam.NewService(baseUrl, clientId, clientSecret)

	app.Use(func(c *fiber.Ctx) error {
		jwtToken := c.Get("Authorization")
		if jwtToken == "" {
			return c.Status(fiber.StatusUnauthorized).SendString("Unauthorized")
		}
		if !strings.HasPrefix(jwtToken, "Bearer ") {
			return c.Status(fiber.StatusUnauthorized).SendString("Unauthorized")
		}
		token := strings.TrimPrefix(jwtToken, "Bearer ")
		// Middleware to handle authentication
		user, err := service.Me(c.Context(), token)
		if err != nil {
			return c.Status(fiber.StatusUnauthorized).SendString("Unauthorized")
		}
		c.Locals("user", user)
		return c.Next()
	})

	app.Get("/", func(c *fiber.Ctx) error {
		return c.SendString(fmt.Sprintf("Hello, %s!", c.Locals("user").(*goiam.User).Name))
	})

	err := app.Listen(":3001")
	if err != nil {
		log.Fatal(err)
		return
	}
}
