

# Base image
 
FROM node:16
 
# Set the working directory in the container
 
WORKDIR /usr/src/app
# Copy package.json and package-lock.json to the container
 
COPY package.json ./
 
# Install dependencies
 
RUN npm install
 
# Copy the rest of the app files
 
COPY . .
 
# Expose port 4567
 
EXPOSE 4567
 
# Command to start the app
 
CMD ["node", "express.js"]
 


