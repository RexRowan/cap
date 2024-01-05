# Use an official Node runtime as a parent image
FROM node:14

# Set work directory
WORKDIR /usr/src/app

# Install dependencies
COPY package.json package-lock.json ./  
RUN npm install

# Copy project files
COPY . .

# Build the app
RUN npm run build

# Install `serve` to serve the app on port 3000
RUN npm install -g serve

# Expose the port the app runs on
EXPOSE 3000

# Run the application
CMD ["serve", "-s", "build", "-l", "3000"]
