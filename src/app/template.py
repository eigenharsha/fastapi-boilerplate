from src.config.settings import get_settings


settings = get_settings()

landing_page = f"""
            <html>
                <head>
                    <title>{settings.APP_NAME}</title>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <style>
                        body {{
                            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
                            line-height: 1.6;
                            margin: 0;
                            padding: 0;
                            color: #333;
                        }}
                        .container {{
                            max-width: 1200px;
                            margin: 0 auto;
                            padding: 2rem;
                        }}
                        .header {{
                            background: linear-gradient(135deg, #1a237e, #0d47a1);
                            color: white;
                            padding: 3rem 0;
                            text-align: center;
                        }}
                        .header h1 {{
                            margin: 0;
                            font-size: 2.5rem;
                            font-weight: 600;
                        }}
                        .version-badge {{
                            background: rgba(255, 255, 255, 0.1);
                            padding: 0.5rem 1rem;
                            border-radius: 20px;
                            font-size: 0.9rem;
                            margin-top: 1rem;
                            display: inline-block;
                        }}
                        .content {{
                            padding: 2rem 0;
                        }}
                        .card {{
                            background: white;
                            border-radius: 8px;
                            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                            padding: 1.5rem;
                            margin-bottom: 1.5rem;
                        }}
                        .links {{
                            display: grid;
                            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                            gap: 1.5rem;
                            margin-top: 2rem;
                        }}
                        .link-card {{
                            background: white;
                            border-radius: 8px;
                            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                            padding: 1.5rem;
                            transition: transform 0.2s;
                        }}
                        .link-card:hover {{
                            transform: translateY(-3px);
                        }}
                        .link-card h3 {{
                            margin: 0 0 0.5rem 0;
                            color: #1a237e;
                        }}
                        .link-card p {{
                            margin: 0;
                            color: #666;
                        }}
                        .link-card a {{
                            display: inline-block;
                            margin-top: 1rem;
                            color: #1a237e;
                            text-decoration: none;
                            font-weight: 500;
                        }}
                        .link-card a:hover {{
                            text-decoration: underline;
                        }}
                    </style>
                </head>
                <body>
                    <div class="header">
                        <div class="container">
                            <h1>{settings.APP_NAME}</h1>
                            <div class="version-badge">Version {settings.APP_VERSION}</div>
                        </div>
                    </div>
                    
                    <div class="container">
                        <div class="content">
                            <div class="card">
                                <h2>About</h2>
                                <p>{settings.APP_DESCRIPTION}</p>
                            </div>
                            
                            <div class="links">
                                <div class="link-card">
                                    <h3>API Documentation</h3>
                                    <p>Explore our interactive API documentation with Swagger UI.</p>
                                    <a href="/docs">View Swagger Docs →</a>
                                </div>
                                
                                <div class="link-card">
                                    <h3>ReDoc Documentation</h3>
                                    <p>Alternative API documentation with a clean, responsive interface.</p>
                                    <a href="/redoc">View ReDoc →</a>
                                </div>
                                
                                <div class="link-card">
                                    <h3>Health Check</h3>
                                    <p>Check the current status and health of the API.</p>
                                    <a href="/api/v1/health">View Health Status →</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </body>
            </html>
            """