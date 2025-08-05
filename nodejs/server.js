const express = require("express");
const { GoIamSdk } = require("@goiam/typescript");

const app = express();

// Configuration
const config = {
  baseUrl: "http://localhost:3000",
  clientId: "abcdef1234567890abcdef1234567890",
  clientSecret: "abcdef1234567890abcdef1234567890",
  port: 3002,
};

// Initialize Go IAM service
const goiamService = new GoIamSdk(
  config.baseUrl,
  config.clientId,
  config.clientSecret
);

// Middleware to parse JSON
app.use(express.json());

// Authentication middleware
const authenticateToken = async (req, res, next) => {
  const authHeader = req.headers["authorization"];
  const token = authHeader && authHeader.split(" ")[1]; // Bearer TOKEN

  if (!token) {
    return res.status(401).json({ error: "Unauthorized - No token provided" });
  }

  try {
    // Validate token with Go IAM service
    const user = await goiamService.me(token);

    // Store user information in request object
    req.user = user;
    next();
  } catch (error) {
    console.error("Token validation error:", error.message);
    return res.status(401).json({ error: "Unauthorized - Invalid token" });
  }
};

// Apply authentication middleware to all routes
app.use(authenticateToken);

// Protected route
app.get("/", (req, res) => {
  res.json({
    message: `Hello, ${req.user.name}!`,
    user: req.user,
  });
});

// Health check endpoint (also protected in this example)
app.get("/health", (req, res) => {
  res.json({
    status: "healthy",
    user: req.user.name,
    timestamp: new Date().toISOString(),
  });
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error("Server error:", err);
  res.status(500).json({ error: "Internal server error" });
});

// Start server
app.listen(config.port, () => {
  console.log(
    `Go IAM Node.js example server running on http://localhost:${config.port}`
  );
  console.log(`Make sure Go IAM server is running on ${config.baseUrl}`);
});

module.exports = app;
