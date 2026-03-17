module.exports = {
    // Configurações do servidor
    port: process.env.PORT || 3000,
    
    // JWT
    jwtSecret: process.env.JWT_SECRET || '2ur8q32ur832urpqujçOIFHAEW9HDQEFGQ328DHAEUIYFOCBSYUGQ9',
    jwtExpiration: '24h',
    
    // Rate limiting
    rateLimit: {
        windowMs: 15 * 60 * 1000, // 15 minutos
        max: 1000 // máximo 1000 requests por IP
    }
};