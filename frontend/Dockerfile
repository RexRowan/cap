# Use an official Node runtime as a parent image
FROM node:14

# Set work directory
WORKDIR /usr/src/app

# Ensure that we run as root to avoid permission issues
USER root

# Install dependencies
# Ensure package.json and package-lock.json are copied where available
COPY package*.json ./

# Clear npm cache and install dependencies
RUN npm cache clean --force && npm install

# Copy project files
COPY . .

# Build the app using npx to avoid any global install issues
RUN npx react-scripts build

# Install `serve` to serve the app on port 3000
# Use the --unsafe-perm flag to avoid permission issues when installing global packages
RUN npm install -g serve --unsafe-perm

# Expose the port the app runs on
EXPOSE 3000

# Run the application
CMD ["serve", "-s", "build", "-l", "3000"]
