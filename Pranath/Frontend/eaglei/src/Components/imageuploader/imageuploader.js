import React from 'react';
import ImageUploader from 'react-images-upload';
 
class imageuploader extends React.Component {
 
    constructor(props) {
        super(props);
         this.state = { pictures: [] };
         this.onDrop = this.onDrop.bind(this);
    }
 
    onDrop(picture) {
        this.setState({
            pictures: this.state.pictures.concat(picture),
        });
    }
 
    render() {
        return (
            <ImageUploader
                withIcon={true}
                onChange={this.onDrop}
                imgExtension={['.jpg', '.gif', '.png', '.gif', '.svg']}
                maxFileSize={5242880}
            />
        );
    }
}

export default imageuploader;