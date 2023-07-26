import React from 'react';

const MainImage = ({ imageUrl, is_updated }) => {
  console.log(is_updated)
  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', width: '60vw', height: 'auto', marginTop: '50px' }}>
      {imageUrl && is_updated && <img src={`${imageUrl}?${is_updated}`} alt="Uploaded" style={{ maxWidth: '100%', maxHeight: '100%' }} />}
    </div>
  );
};

export default MainImage;