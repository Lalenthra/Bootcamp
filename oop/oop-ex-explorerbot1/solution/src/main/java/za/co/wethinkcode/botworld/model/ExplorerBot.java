package za.co.wethinkcode.botworld.model;

import static java.lang.Math.*;

public class ExplorerBot
{
    public static final int WORLD_MAX_X = 10;
    public static final int WORLD_MAX_Y = 10;

    private int x;
    private int y;
    private Heading heading = Heading.N;

    public ExplorerBot( int initialX, int initialY ){
        x = checkInsideWorldWidth( initialX );
        y = checkInsideWorldHeight( initialY );
    }

    /**
     * Turn the receiver bot to a new heading.
     * @param newHeading
     */
    public void turnTo( Heading newHeading ){
        heading = newHeading;
    }

    /**
     * Answer the receiver bot's current heading.
     * @return a Heading
     */
    public Heading heading(){
        return heading;
    }

    /**
     * Answer the receiver's current x-position in the world.
     * @return An int not less than 0, and not larger than the world width
     */
    public int xPosition(){
        return x;
    }

    /**
     * Answer the receiver's current y-position in the world.
     * @return An int not less than 0, and not larger than the world height
     */
    public int yPosition(){
        return y;
    }

    /**
     * Move the receiver bot 1 klik in the direction it currently faces but not
     * beyond the edges of the world.
     */
    public void move(){
        switch( heading() ){
            case N -> y = max( 0, --y );
            case S -> y = min( WORLD_MAX_Y, ++y );
            case W -> x = max( 0, --x );
            case E -> x = min( WORLD_MAX_X, ++x );
        }
    }

    private int checkInsideWorldWidth( int v ){
        if( v < 0 || v > WORLD_MAX_X ) throw new IllegalArgumentException();
        return v;
    }

    private int checkInsideWorldHeight( int v ){
        if( v < 0 || v > WORLD_MAX_Y ) throw new IllegalArgumentException();
        return v;
    }
}
