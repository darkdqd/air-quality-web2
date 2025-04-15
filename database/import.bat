@echo off
mysql -h crossover-proxy.rlwy.net -u root -p --port 45228 railway < air_quality_schema.sql
