import axios, { AxiosResponse } from 'axios';
import dotenv from 'dotenv';

// Load environment variables
dotenv.config();

// Types for the API responses
interface UserResponse {
    message: string;
    user: any; // Replace with proper User type from @goiam/typescript when available
}

interface HealthResponse {
    status: string;
    user: string;
    timestamp: string;
}

interface ProfileResponse {
    profile: any; // Replace with proper User type from @goiam/typescript when available
    timestamp: string;
}

// Configuration
const CONFIG = {
    SERVER_URL: process.env.SERVER_URL || 'http://localhost:3003',
    JWT_TOKEN: process.env.JWT_TOKEN || '<your_jwt_token>',
} as const;

// HTTP client configuration
const createAuthHeaders = (token: string) => ({
    'Authorization': `Bearer ${token}`,
    'Content-Type': 'application/json',
});

// Test functions
async function testMainEndpoint(): Promise<void> {
    try {
        console.log('Testing main endpoint...');
        const response: AxiosResponse<UserResponse> = await axios.get(
            `${CONFIG.SERVER_URL}/`,
            {
                headers: createAuthHeaders(CONFIG.JWT_TOKEN),
            }
        );

        console.log('✅ Main endpoint successful!');
        console.log('Response:', response.data);
    } catch (error) {
        console.error('❌ Main endpoint failed:', axios.isAxiosError(error)
            ? error.response?.data
            : error
        );
    }
}

async function testHealthEndpoint(): Promise<void> {
    try {
        console.log('\nTesting health endpoint...');
        const response: AxiosResponse<HealthResponse> = await axios.get(
            `${CONFIG.SERVER_URL}/health`,
            {
                headers: createAuthHeaders(CONFIG.JWT_TOKEN),
            }
        );

        console.log('✅ Health endpoint successful!');
        console.log('Response:', response.data);
    } catch (error) {
        console.error('❌ Health endpoint failed:', axios.isAxiosError(error)
            ? error.response?.data
            : error
        );
    }
}

async function testProfileEndpoint(): Promise<void> {
    try {
        console.log('\nTesting profile endpoint...');
        const response: AxiosResponse<ProfileResponse> = await axios.get(
            `${CONFIG.SERVER_URL}/profile`,
            {
                headers: createAuthHeaders(CONFIG.JWT_TOKEN),
            }
        );

        console.log('✅ Profile endpoint successful!');
        console.log('Response:', response.data);
    } catch (error) {
        console.error('❌ Profile endpoint failed:', axios.isAxiosError(error)
            ? error.response?.data
            : error
        );
    }
}

// Main test function
async function runTests(): Promise<void> {
    console.log('🚀 Starting Go IAM TypeScript client tests...\n');

    if (CONFIG.JWT_TOKEN === '<your_jwt_token>' || !CONFIG.JWT_TOKEN) {
        console.error('❌ JWT_TOKEN environment variable is not set or is using the default placeholder');
        console.log('\nTo set up the JWT token:');
        console.log('1. Login to Go IAM web interface');
        console.log('2. Open browser Developer Tools');
        console.log('3. Go to Application/Storage tab');
        console.log('4. Find "access_token" in Local Storage');
        console.log('5. Copy the token value');
        console.log('6. Set the environment variable: export JWT_TOKEN=your_actual_token');
        console.log('7. Or create/update a .env file with: JWT_TOKEN=your_actual_token');
        console.log('8. Re-run the client: npm run client');
        return;
    }

    console.log(`🔗 Server URL: ${CONFIG.SERVER_URL}`);
    console.log(`🔑 Using JWT token: ${CONFIG.JWT_TOKEN.substring(0, 20)}...`);

    try {
        await testMainEndpoint();
        await testHealthEndpoint();
        await testProfileEndpoint();

        console.log('\n🎉 All tests completed!');
    } catch (error) {
        console.error('\n💥 Unexpected error during testing:', error);
    }

    console.log('\nTroubleshooting tips:');
    console.log('• Ensure the TypeScript server is running: npm run dev');
    console.log('• Verify Go IAM server is running on http://localhost:3000');
    console.log('• Check that your JWT token is valid and not expired');
    console.log(`• Make sure the server is accessible on ${CONFIG.SERVER_URL}`);
    console.log('• Verify environment variables: echo $JWT_TOKEN');
}

// Error handling for unhandled promise rejections
process.on('unhandledRejection', (reason, promise) => {
    console.error('Unhandled Rejection at:', promise, 'reason:', reason);
    process.exit(1);
});

// Run the tests
runTests().catch((error) => {
    console.error('Failed to run tests:', error);
    process.exit(1);
});
