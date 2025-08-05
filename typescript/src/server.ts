import express, { Request, Response, NextFunction } from 'express';
import { GoIamSdk } from '@goiam/typescript';
import dotenv from 'dotenv';

// Load environment variables
dotenv.config();

const app = express();

// Configuration interface
interface Config {
    baseUrl: string;
    clientId: string;
    clientSecret: string;
    port: number;
}

// Configuration
const config: Config = {
    baseUrl: process.env.GO_IAM_BASE_URL || 'http://localhost:3000',
    clientId: process.env.GO_IAM_CLIENT_ID || 'abcdef1234567890abcdef1234567890',
    clientSecret: process.env.GO_IAM_CLIENT_SECRET || 'abcdef1234567890abcdef1234567890',
    port: parseInt(process.env.SERVER_PORT || '3003', 10),
};

// Initialize Go IAM service
const goiamService = new GoIamSdk(
    config.baseUrl,
    config.clientId,
    config.clientSecret
);

// Extend Request interface to include user
declare global {
    namespace Express {
        interface Request {
            user?: any; // Replace with proper User type from @goiam/typescript when available
        }
    }
}

// Middleware to parse JSON
app.use(express.json());

// Authentication middleware
const authenticateToken = async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    const authHeader = req.headers.authorization;
    const token = authHeader?.split(' ')[1]; // Bearer TOKEN

    if (!token) {
        res.status(401).json({ error: 'Unauthorized - No token provided' });
        return;
    }

    try {
        // Validate token with Go IAM service
        const user = await goiamService.me(token);

        // Store user information in request object
        req.user = user;
        next();
    } catch (error) {
        console.error('Token validation error:', error instanceof Error ? error.message : 'Unknown error');
        res.status(401).json({ error: 'Unauthorized - Invalid token' });
    }
};

// Apply authentication middleware to all routes
app.use(authenticateToken);

// Protected route
app.get('/', (req: Request, res: Response): void => {
    res.json({
        message: `Hello, ${req.user?.name || 'User'}!`,
        user: req.user,
    });
});

// Health check endpoint (also protected in this example)
app.get('/health', (req: Request, res: Response): void => {
    res.json({
        status: 'healthy',
        user: req.user?.name || 'Unknown',
        timestamp: new Date().toISOString(),
    });
});

// User profile endpoint
app.get('/profile', (req: Request, res: Response): void => {
    res.json({
        profile: req.user,
        timestamp: new Date().toISOString(),
    });
});

// Error handling middleware
app.use((err: Error, req: Request, res: Response, next: NextFunction): void => {
    console.error('Server error:', err);
    res.status(500).json({ error: 'Internal server error' });
});

// Start server
app.listen(config.port, (): void => {
    console.log(`Go IAM TypeScript example server running on http://localhost:${config.port}`);
    console.log(`Make sure Go IAM server is running on ${config.baseUrl}`);
    console.log('Environment:', process.env.NODE_ENV || 'development');
});

export default app;
