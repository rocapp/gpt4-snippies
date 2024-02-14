// Function to handle the extraction and storage of image URLs
const storeImageURLs = (() => {
    const observedImageURLs = new Set(); // Stores unique image URLs
  
    // Function to process mutations and extract image URLs
    const processMutations = (mutations) => {
      mutations.forEach((mutation) => {
        mutation.addedNodes.forEach((node) => {
          // Check if the added node is an image or contains images
          if (node.nodeType === 1) { // ELEMENT_NODE
            const images = node.tagName === 'IMG' ? [node] : node.querySelectorAll('img');
            images.forEach((img) => {
              if (img.src && !observedImageURLs.has(img.src)) {
                observedImageURLs.add(img.src);
                console.log(`New image URL stored: ${img.src}`);
                // Here, you can also call a function to do something with the new image URL
              }
            });
          }
        });
      });
    };
  
    // Create an observer instance with a callback function to execute when mutations are observed
    const observer = new MutationObserver(processMutations);
  
    // Configuration of the observer:
    const config = { childList: true, subtree: true };
  
    // Start observing the document body for DOM mutations
    observer.observe(document.body, config);
  
    // Public API to access the stored URLs
    return {
      getStoredURLs: () => Array.from(observedImageURLs),
    };
  })();
  
  // Example: Accessing stored URLs
  // You might want to expose a method to retrieve these URLs, or integrate with your existing logic
  setTimeout(() => {
    console.log('Stored image URLs:', storeImageURLs.getStoredURLs());
  }, 5000); // Adjust the timing based on your application's needs
  